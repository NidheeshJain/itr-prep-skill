# Phase 7 — Output: Data-Pack JSON and Verifying a Portal JSON

## Deliverable A — the data pack (default output)

One annotated JSON file the user can hand to any assistant (or read themselves) to fill the portal
mechanically. Save to the user's Downloads/working directory, named
`ITR_datapack_<PAN>_AY<year>.json`. Validate it parses after writing.

Required top-level sections (include only those relevant to the profile, but never omit a relevant one):

```jsonc
{
  "_README": "what this is, AY, form, who prepared it, reconciliation status",
  "rules_verification": { "one row per rate/limit/date used anywhere in this pack:
                           { rule, value_used, source_url, checked_on } — e.g. slab table, standard
                           deduction, 87A threshold, CG rates, 112A exemption, surcharge tiers, audit
                           limit, due date. Official sources (incometaxindia.gov.in / incometax.gov.in)
                           preferred; a rule with no row here means it was NOT verified — fix before
                           delivering" },
  "meta": { "assessment_year", "form": "ITR-1|2|3|4", "regime", "regime_action (10-IEA needed or not)",
             "filing_section": "139(1)", "due_date", "due_date_consequences" },
  "taxpayer": { "name", "pan", "dob", "aadhaar: TODO", "address", "email", "mobile: TODO",
                 "residential_status + basis", "bank_accounts[] (no, IFSC, refund-nominee flag)" },
  "salary":   { "employers[] (name, tan, period, gross 17(1)/(2)/(3), component breakup,
                 employer regime, quarterly TDS w/ receipt numbers)",
                 "exemptions_sec10 (item, amount, statutory basis)",
                 "totals (single standard deduction!)" },
  "house_property": {},
  "capital_gains": { "per bucket: scripwise rows (ISIN, qty, cost, consideration, dates), intra-CG set-off,
                      quarterwise gains, net + carry-forward" },
  "business_fno": { "classification, turnover, audit determination + reasoning, gross P&L,
                     itemized expenses, net, nature-of-business code" },
  "other_sources": { "interest per account, dividend (quarterwise), refund interest 244A, family pension…" },
  "foreign": { "schedule FA rows, FSI, FTC + Form 67 status" },
  "brought_forward_losses": { "per-AY vintage from prior ITR's ScheduleCFL/ScheduleUD: type, opening
                               amount, absorbed this year, closing, expiry AY; source: filed JSON or
                               143(1) intimation" },
  "setoff_cyla_bfla": { "explicit set-off trail: what absorbed what" },
  "losses_carried_forward": { "per vintage, with the file-by-due-date condition stated" },
  "deductions_via": { "per section, only regime-valid ones counted; others listed as not-claimable" },
  "tax_computation": { "slab walk, special-rate items, rebate, surcharge+marginal relief, cess, total" },
  "taxes_paid": { "TDS rows (TAN, amount), TCS, advance tax challans, SAT challans w/ CIN" },
  "balance_and_interest": { "assessed tax, 234A/B/C with month counts, TOTAL TO PAY, cost-of-delay per month" },
  "ais_reconciliation": { "per-item match status; every unresolved item as an explicit VERIFY flag" },
  "verification_checklist_before_submit": [ "SAT paid + CIN entered", "e-verify within 30 days", "…" ]
}
```

Conventions: amounts INR integers (paise only where source has them), dates YYYY-MM-DD, every figure
traceable to the Phase 2/3 ledger, `TODO`/`VERIFY` prefixes for anything only the user can confirm.
The final chat message must list all open TODO/VERIFY items — the pack is not "done" while any remain.

## Deliverable B — verifying an official ITR JSON (portal/utility export)

The portal's JSON is `{"ITR": {"ITR3": {...schedules...}}}` (or ITR1/2/4). Schedule names:
`PartA_GEN1` (personal + filing status + regime flags `Form10IEAEarlierAYOldRegime`/`F10IEACurrAYOldRegime`),
`ScheduleS`, `ScheduleHP`, `ScheduleCGFor23` + `ScheduleSI` (special incomes), `ITR3ScheduleBP`,
`PARTA_PL`/`TradingAccount`/`PARTA_BS`, `ScheduleOS`, `ScheduleCYLA/BFLA/CFL`, `ScheduleVIA`,
`ScheduleFA/FSI/TR`, `ScheduleTDS1/TDS2/TCS/IT`, `PartB-TI`, `PartB_TTI`, `Verification`.

Verification procedure:
1. Parse and extract every material leaf: salary per TAN, exemptions, each OS line, CG rows, BP totals,
   CYLA/CFL, `PartB-TI.TotalIncome`, `PartB_TTI` tax/interest/`BalTaxPayable`, bank accounts, TDS rows.
2. **Recompute independently from source documents** (never from the JSON's own intermediate figures)
   and diff line by line.
3. For every mismatch report: field, JSON value, your value, source evidence, ₹ impact, and whether it
   over- or under-reports income. A figure in the JSON with NO source (e.g., an interest line you can't
   find in AIS/26AS) is a first-class finding — ask the user, don't assume either way; it may come from
   a source you weren't given (26AS refund interest is the classic).
4. Check structural traps: single standard deduction; regime flags consistent with the chosen regime;
   losses in CFL only if due date holds; `SelfAssessmentTax` > 0 and CIN present if there was a payable;
   dividend quarterwise filled; 112A scripwise present; Chapter VI-A total ≤ gross total income and
   nothing regime-invalid claimed; **Schedule AL present if total income exceeds its threshold**;
   Schedule FA present if ROR with foreign assets; TCS credits from 26AS claimed; agri > ₹5,000 not
   sitting in an ITR-1/4.
5. When two JSONs exist (user edited something), flat-diff them (`old vs new leaves`) and report what
   changed, whether it was needed, and the ₹ impact — users often make cosmetic edits they think are
   substantive and vice versa.

## Handing off to a browser assistant

When the user will fill the portal with an AI browser assistant, tell them to include with the JSON:
"Fill each schedule using these exact figures; follow `verification_checklist_before_submit`;
STOP before final submission for my review." The pack's annotations are written to survive that handoff.
