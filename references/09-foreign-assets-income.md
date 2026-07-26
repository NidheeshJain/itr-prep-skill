# Phase 4 — Foreign Assets and Income (Schedules FA / FSI / TR, Form 67)

Applies only to **ROR** residents (RNOR/NR skip Schedule FA — but confirm residency carefully first,
reference 01). Non-disclosure of foreign assets carries Black Money Act penalties (₹10L per failure) —
this is the highest-stakes schedule in the return; never let a user skip it because "it's small".

## Schedule FA — what to report (holdings, not just sales)

Report if held **at any time** during the relevant period (Schedule FA uses the **calendar year**
ending in the FY — e.g., for FY 2025-26 report CY 2025; verify current instruction):

| Table | Asset | Typical case |
|---|---|---|
| A1/A2 | Foreign bank/custodial accounts | E*TRADE/Schwab cash account from RSUs — YES it counts |
| A3 | Foreign equity & debt | **RSUs/ESPPs of foreign parent (vested), foreign stocks bought via apps (INDmoney etc.)** |
| A4 | Foreign insurance/annuity | |
| B/C/D | Financial interest, immovable property, other assets, signing authority | |

Per row: country, entity name+address, dates, **peak value**, closing value, income accrued — in INR at
prescribed conversion (SBI TT buying rate; verify current rule). Get these from the broker's annual
statement. Unvested RSUs are NOT reportable; vested-but-unsold ARE.

## Foreign income (Schedule FSI) + DTAA relief (Schedule TR + Form 67)

- Foreign dividends (e.g., on US stock): taxable at slab in India; US withholds 25% under treaty.
- Foreign CG on sale: normal Indian CG rules (unlisted-foreign-share holding periods apply).
- Claim foreign tax credit: report country-wise in FSI, treaty article in TR, and **file Form 67
  before/with the return** — FTC is routinely denied without it. Credit = lower of foreign tax paid
  and Indian tax on that income.
- US RSU double-tax confusion: the vest was taxed as salary in India (17(2) perquisite); on sale only
  the gain ABOVE the vest-date FMV is Indian CG. Cost basis = FMV at vest, not zero.

### FSI column (d) — "tax payable on such income under normal provisions in India"

Not auto-populated from Form 67 — you compute it, and the identical figure must be entered
independently in both Schedule FSI and Form 67 (they aren't linked electronically; a mismatch between
them can delay or reject the FTC claim).

- Formula (Sec 2(10) "average rate of tax", applied per Rule 128): `average rate = total tax liability
  (incl. surcharge + cess, computed before FTC relief) ÷ total income (Part B-TI)`; column (d) =
  average rate × foreign-source income included in total income.
- Column (e) relief = lower of (c) tax paid abroad and (d) — usually (c), since (d) often comes out
  higher than the foreign withholding.
- Cross-check the FTC amount against any withholding certificate the payer/broker issues (e.g. a US
  1042-S) if one is available — a mismatch flags either a wrong conversion-rate lookup or an
  incomplete foreign-income figure, not just a rounding difference.

### Table A3 — one row per tranche, or one aggregated row per company?

Technically precise is one row per distinct acquisition date (each vest/purchase tranche has its own
initial/peak/closing value). Aggregating to a single row per company is common practice when the
portal doesn't cleanly support multiple rows per entity — state the tradeoff to the user and let them
choose, then document which was done and why in the data pack.

When the broker only gives an annual/summary dividend figure per security (no per-tranche or
per-quarter split, but the schedule — or the user's own reporting preference — wants one):
reconstruct it by **proportional allocation by share count**. Dividend-per-share is uniform across
tranches regardless of vest/purchase date, so splitting the total by each tranche's share count is
exact, not an approximation — as long as all tranches are the same share class. For a per-payment
(quarterly) breakdown, get the actual payment dates from the broker's dividend/cash-transaction
history and pro-rate each individual payment across tranches by shares held on that payment's
record date, rather than pro-rating only the annual total.

### Sourcing the entity's registered address (Table A3/B)

Broker statements frequently omit the issuer's registered address. Don't fill it from memory — pull
it from the entity's own regulatory filing (e.g. a US-listed company's 10-K cover page) or its
investor-relations page, and note the source, same as any other verified fact.

### Custodial account vs. direct holding (A2 vs. A3) for employer RSU/ESPP brokerage accounts

An employer-linked equity-award brokerage blurs the A2 (custodial account)/A3 (direct equity holding)
line. Common practice: report the underlying shares under A3 with the issuing company as the entity,
and don't also duplicate the same value under A2 as a separate custodial account — verify current
portal guidance if unsure, and record whichever choice was made.

## Practical workflow

1. Ask for the foreign brokerage's annual statement + any foreign withholding certificate (e.g. US
   1042-S) — the certificate doubles as a cross-check for the FTC figure, not just a data source.
2. Build the FA rows account-by-account; peak balance needs monthly statements or the broker's summary.
3. Convert at the prescribed rate; keep the conversion working in the data pack.
4. If foreign tax was withheld, compute FTC (see FSI column (d) above) and remind about Form 67
   explicitly in the checklist.
5. If this year's document review surfaces a **prior filed year's** foreign income that was never
   reported, don't fold it silently into the current year — treat it as a separate compliance-gap
   decision (Sec 139(8A) updated return window/tax tiers, Black Money Act Sec 43 penalty exposure and
   its de-minimis exemption, Sec 149 extended reassessment window for foreign-asset income). Disclose
   the risk plainly, let the user decide whether to correct the prior year, and record the decision —
   don't make the call for them.
