# itr-prep-skill — Claude Code skill for Indian Income Tax Returns (ITR-1/2/3/4)

A Claude Code skill that takes a user from raw documents (Form 16, AIS, Form 26AS, broker Tax P&L,
payslips) to a fully reconciled, schedule-by-schedule computation and a **portal-ready data-pack JSON**
— designed to be handed to another agent (or a human) that fills the e-filing portal.

## Scope

- Form selection (ITR-1/2/3/4), old-vs-new regime comparison by actual computation
- Multi-employer salary (regime rebuild, single standard deduction, 10(10AA) etc.)
- Capital gains (equity/debt/property/gold/crypto-VDA), F&O & business income, audit applicability
- Loss set-off + carry-forward (CYLA/BFLA/CFL, prior-year ITR parsing, Schedule UD)
- Foreign assets/income (Schedule FA/FSI/TR, Form 67)
- Interest 234A/B/C, AIS/26AS reconciliation, verification of a drafted portal JSON
- **Output boundary: the annotated data-pack JSON.** Portal data entry is intentionally out of scope.

Rates/limits in the reference files are treated as *shape, not truth* — the skill mandates verifying
every rate against official sources (incometaxindia.gov.in / incometax.gov.in) per assessment year and
recording them in a `rules_verification` block in the output.

## Install

```bash
git clone https://github.com/NidheeshJain/itr-prep-skill.git ~/.claude/skills/itr-prep-skill
pip install pycryptodome   # for scripts/decrypt_ais.py (AIS JSON decryption)
```

## Layout

- `SKILL.md` — 8-phase workflow orchestrator
- `references/01–10` — per-domain depth, loaded lazily by profile
- `scripts/decrypt_ais.py` — decrypts the portal's encrypted AIS JSON (PAN + DOB)

## Disclaimer

This is a careful preparer, not a chartered accountant. Users remain legally responsible for filed
figures. Audit cases, HUF/deceased filings, and contested notices are explicitly escalated to a CA.

## Handing off to the filling agent

The data pack is designed to be consumed by a second agent with browser access (e.g. Claude in Chrome
or a cowork session). Attach the data-pack JSON (and optionally the raw documents for spot-checks) with
a prompt like:

```text
I need you to fill my Indian Income Tax Return on https://eportal.incometax.gov.in using the attached
data pack: ITR_datapack_<PAN>_AY<year>.json. It was prepared by another agent after full reconciliation
of my Form 16s, AIS, 26AS and broker statements — treat its figures as authoritative and fill each
schedule with these EXACT numbers. The JSON's comments explain where each figure goes.

Rules:
1. I will log in myself — never ask for or handle my password or OTP.
2. Work schedule by schedule in the portal's Return Summary; after editing any schedule, re-confirm
   downstream schedules (the portal silently un-confirms them).
3. The portal pre-fills from AIS — where pre-fill disagrees with the data pack, the data pack wins;
   tell me about any disagreement instead of silently accepting either.
4. Resolve every item in `verification_checklist_before_submit` and every TODO/VERIFY flag with me
   before proceeding.
5. When validation shows 0 errors, STOP. Show me the final computed tax vs the pack's
   `tax_computation` and `balance_and_interest` figures. I will make the payment, click Submit,
   and e-verify myself.
```

If anything in the pack looks wrong mid-fill, the filling agent should stop and flag it — the pack
carries source attribution for every figure so discrepancies can be traced.

## Contributing

Field reports from real filings are the most valuable contribution — see [CONTRIBUTING.md](CONTRIBUTING.md).
Licensed under [MIT](LICENSE).
