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

## Contributing

Field reports from real filings are the most valuable contribution — see [CONTRIBUTING.md](CONTRIBUTING.md).
Licensed under [MIT](LICENSE).
