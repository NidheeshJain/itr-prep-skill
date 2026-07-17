# Phase 2 — Documents: What to Collect and How to Parse

## Tailored checklist (only ask for what the profile needs)

| Profile element | Documents |
|---|---|
| Always | PAN, Aadhaar (linked), portal login, ALL bank accounts + IFSC, last year's ITR (if any) |
| Salaried | Form 16 (Part A + B) from EVERY employer in the FY; final payslip if Form 16 unclear on components |
| Reconciliation trio | **AIS** (JSON preferred over PDF — parseable), **TIS**, **Form 26AS** — all from incometax.gov.in |
| Shares/MF | Broker **Tax P&L** statement (Zerodha Console → Reports → Tax P&L; equivalents: Groww/Upstox tax reports; CAMS/KFintech consolidated CG statement for MF) |
| F&O/intraday | Same Tax P&L (has turnover + charges) + ledger/other-debits report for account-level charges |
| Crypto | Exchange tax reports (coin-wise, with TDS u/s 194S) |
| Property sale | Sale deed, purchase deed, improvement bills, TDS certificate (194-IA), stamp-duty value |
| Rent received | Rent amounts, tenant PAN if TDS deducted (194-IB), municipal taxes paid, home-loan interest cert |
| Interest | Bank interest certificates (or rely on AIS, cross-checked) |
| Foreign | Brokerage statements (E*TRADE/Schwab/Fidelity…), RSU vesting statements, foreign bank statements, Form 67 if claiming foreign tax credit |
| Deductions (old regime) | 80C proofs, 80D premiums, 80E interest certificate, 80G receipts (with donee PAN), home-loan interest certificate, NPS statements |
| Refund interest | Check 26AS for interest u/s 244A if a refund was received during the FY — it is taxable and users always forget it |

## Parsing notes per document

### AIS JSON (encrypted)
The portal's AIS JSON download is AES-encrypted. Run `scripts/decrypt_ais.py <file> <PAN> <DOB ddmmyyyy>`
(requires `pycryptodome`). Password = lowercase PAN + utility-version middle string + DOB; the script tries
known variants. Output: `*_decrypted.json`.

Structure: `partB.sections[]` → each section has `elements[]` → each element has `title` (e.g. "Salary",
"Interest from savings bank", "Dividend", "Sale of securities and units of mutual fund"), `infoSrcId`
(deductor TAN / reporting-entity ID), and `l1.columnLabel[]/columnData[]` (field-name/value rows).
Amounts are comma-formatted strings; dates are DD/MM/YYYY. Extract per-source, don't just take totals —
per-TAN salary rows are how you detect multiple employers the user forgot to mention.

Sections to mine: **B1 TDS/TCS** (salary + non-salary TDS), **B2 SFT** (interest, dividend, securities
trades, large deposits/"miscellaneous payment" — the latter are usually NOT income), **B3 taxes paid**,
**B4 demand/refund**, **Other information** (per-employer gross salary with employment dates — gives the
job-change timeline).

### Form 16 (PDF, per employer)
- **Part A**: TAN, PAN, period of employment, quarterly amount-paid + TDS table, challan details. The TDS
  total here is the number that must match 26AS/AIS.
- **Part B (Annexure)**: gross 17(1)/17(2)/17(3) split, Sec 10 exemptions (leave encashment, gratuity,
  HRA…), Sec 16 deductions, Chapter VI-A the employer applied, and — critically — the line
  **"Whether opting out of taxation u/s 115BAC(1A)?"** (No = new regime, Yes = old). Record this per
  employer; mixed answers across employers is common after a job change.
- **Salary annexure** (often last page): component breakup (basic, HRA, special, leave encashment,
  bonus…). Needed for HRA exemption and 10(10AA) computations — basic is the base for both.
- Form 12BA (perquisites) if present: ESOP/RSU perquisite values live here.

### Broker Tax P&L (Zerodha-style xlsx)
Sheets: `Equity and Non Equity` (intraday/ST/LT/non-equity realized P&L + charges block),
`F&O` (options/futures P&L + **turnover** + charges block), `Mutual Funds`, `Currency`, `Commodity`,
`Other Debits and Credits` (account-level charges: DP charges, pledge, delayed-payment, DDPI),
`Equity Dividends`, tradewise-exits sheet for scrip-level detail.
- Charges blocks list brokerage/STT/exchange/GST/SEBI/stamp per segment — allocate to the right head
  (see references 04 and 05 for which head takes what).
- The stated F&O "turnover" follows the ICAI method — use it for the audit check rather than recomputing.

### Form 26AS
Flat statement of all TDS/TCS credits + refunds paid (with 244A interest) + advance/SAT challans.
This is the authority for **tax credits**; AIS is the authority for **income the department knows about**.
A TDS entry in Form 16 that is missing from 26AS = employer didn't deposit — warn the user (credit may
be denied; they should chase the employer).

Sweep the **TCS section** too — commonly missed, fully claimable credits: TCS on foreign remittances
under LRS 206C(1G) (forex cards, overseas investing, foreign education fees), on overseas tour packages,
on car purchases > ₹10L. Also check for TDS the user suffered as a payee outside salary: 194A bank
interest, 194 dividend, 194-IB rent (if they're a landlord), 194S crypto. Unclaimed TDS from a prior
year (brought-forward rows in the TDS schedule) and credits stuck under a mismatched/old PAN are worth
asking about when 26AS totals look lower than expected.

### Prior-year ITR (for brought-forward losses)
If the user claims (or might have) carried-forward losses, get last year's **filed ITR JSON** — the
acknowledgment (ITR-V) alone doesn't carry the loss detail. If they've lost it: portal → e-File →
Income Tax Returns → **View Filed Returns** → download the JSON/ITR form. Extract:
- `ScheduleCFL`: per-assessment-year rows of each loss type still alive (HP, non-speculative business,
  speculative, STCL, LTCL) — these become this year's brought-forward opening balances;
- `ScheduleUD`: unabsorbed depreciation (separate from business loss, no expiry);
- check the prior return was filed u/s 139(1) (on time) — a belated original kills the carry-forward
  of most losses, and the 143(1) intimation may have adjusted figures: prefer the intimation's numbers
  if there was one.

## Reconciliation nuggets

- **TDS implies income**: a 26AS TDS row with no matching income in the ledger means a payment reached
  the PAN — find the income; never claim the credit while omitting the receipt.
- **Freelance/platform payouts** (YouTube/Stripe/PayPal/brand deals): sum the payout files AND confirm
  the total against bank credits; avoid double-counting payouts already inside a 26AS 194C/194J entry.
- **Foreign platform paying INR to a resident** = ordinary Indian-source business income, not "foreign
  income" — but a genuine foreign account/asset still triggers Schedule FA (reference 09).

## The working ledger

As you parse, build one table: source document → field → amount → which ITR schedule it lands in.
Present it to the user after Phase 3 reconciliation so they see everything tied out before computation
begins. Every figure in the final data pack must appear in this ledger with a source.
