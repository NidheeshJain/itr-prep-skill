#!/usr/bin/env python3
"""
Decrypt AIS (Annual Information Statement) JSON files
downloaded from the Indian Income Tax portal.

Usage:
    python3 decrypt_ais.py <encrypted_file> <PAN> <DOB>
    python3 decrypt_ais.py <encrypted_file> <PAN> <DOB> [--password-middle VALUE]
    python3 decrypt_ais.py <encrypted_file> <PAN> <DOB> --password VALUE

    PAN  - Your PAN number (e.g. ABCPD1234E)
    DOB  - Date of birth in ddmmyyyy format (e.g. 15061990)
"""

import argparse
import sys
import json
import base64
from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad


PASSWORD_MIDDLE = "GQ39%*g"


def _load_encrypted_payload(filepath):
    raw = Path(filepath).read_text(encoding="utf-8").strip()

    # Some tools export the encrypted AIS string as a JSON string instead of raw text.
    if raw.startswith('"') and raw.endswith('"'):
        raw = json.loads(raw)

    if len(raw) < 64:
        raise ValueError(
            "Encrypted AIS file is too short. Expected IV(32 hex) + salt(32 hex) + ciphertext."
        )

    iv_hex = raw[:32]
    salt_hex = raw[32:64]
    ciphertext_part = raw[64:]

    try:
        iv = bytes.fromhex(iv_hex)
        salt = bytes.fromhex(salt_hex)
    except ValueError as exc:
        raise ValueError(
            "The first 64 characters of the AIS file must be hexadecimal IV + salt."
        ) from exc

    try:
        ciphertext = base64.b64decode(ciphertext_part, validate=True)
    except Exception:
        try:
            ciphertext = bytes.fromhex(ciphertext_part)
        except ValueError as exc:
            raise ValueError(
                "Ciphertext must be valid Base64 or hexadecimal data."
            ) from exc

    if not ciphertext:
        raise ValueError("Ciphertext payload is empty.")

    return iv, salt, ciphertext


def _password_candidates(pan, dob, password_middle=None):
    lower_pan = pan.lower()
    upper_pan = pan.upper()

    candidates = []
    seen = set()

    def add(candidate):
        if candidate not in seen:
            seen.add(candidate)
            candidates.append(candidate)

    if password_middle is not None:
        add(f"{lower_pan}{password_middle}{dob}")
        return candidates

    # Try the currently observed AIS utility format first, then simpler variants.
    add(f"{lower_pan}{PASSWORD_MIDDLE}{dob}")
    add(f"{lower_pan}{dob}")
    add(f"{upper_pan}{dob}")

    return candidates


def _decrypt_with_password(iv, salt, ciphertext, password):
    key = PBKDF2(
        password.encode("utf-8"),
        salt,
        dkLen=32,
        count=1000,
        hmac_hash_module=SHA256,
    )

    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode("utf-8")


def decrypt_ais(filepath, pan, dob, password_middle=None, password=None):
    iv, salt, ciphertext = _load_encrypted_payload(filepath)

    last_error = None
    plaintext = None

    if password is not None:
        password_candidates = [password]
    else:
        password_candidates = _password_candidates(
            pan, dob, password_middle=password_middle
        )

    for candidate in password_candidates:
        try:
            plaintext = _decrypt_with_password(iv, salt, ciphertext, candidate)
            break
        except Exception as exc:
            last_error = exc

    if plaintext is None:
        raise ValueError(
            "Decryption failed. Check PAN, DOB, and that the AIS file is the encrypted utility JSON. "
            "If needed, pass --password-middle explicitly."
        ) from last_error

    try:
        data = json.loads(plaintext)
    except json.JSONDecodeError as exc:
        raise ValueError("Decryption completed but the result was not valid JSON.") from exc

    in_path = Path(filepath)
    out_path = in_path.with_name(f"{in_path.stem}_decrypted.json")
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Decrypted successfully -> {out_path}")
    return str(out_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filepath", help="Path to the encrypted AIS file")
    parser.add_argument("pan", help="PAN number")
    parser.add_argument("dob", help="Date of birth in ddmmyyyy format")
    parser.add_argument(
        "--password-middle",
        default=None,
        help="Optional string inserted between pan.lower() and dob before key derivation",
    )
    parser.add_argument(
        "--password",
        default=None,
        help="Optional full password to use directly for PBKDF2, bypassing password construction",
    )
    args = parser.parse_args()

    decrypt_ais(
        args.filepath,
        args.pan,
        args.dob,
        password_middle=args.password_middle,
        password=args.password,
    )
