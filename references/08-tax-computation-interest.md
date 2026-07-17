# Phase 6 — Tax Computation and Interest (234A/B/C, 234F)

## Computation stack (in order)

1. **Slab tax** on normal-rate income (verify current-AY slabs for the chosen regime — never from memory).
2. **Special-rate taxes** added: 111A STCG, 112/112A LTCG, 115BBH VDA (30%), 115BB lottery — these are
   OUTSIDE the slabs; regime choice does not change them.
3. **Rebate 87A** if total income ≤ threshold (differs sharply by regime — verify; note rebate generally
   does NOT apply against 112A LTCG and special-rate incomes — check current position).
4. **Surcharge** on (tax): tiers by total income (50L/1Cr/2Cr/5Cr — verify rates; new regime caps the top
   tier; CG + dividend surcharge capped at 15%). Apply **marginal relief**: surcharge cannot exceed the
   income above the threshold. Warn users within ~₹2L below a threshold that crossing it is expensive.
5. **Cess 4%** on tax + surcharge.
6. Less: **TDS + TCS + advance tax + self-assessment already paid** (from 26AS).
7. Result: balance payable → interest below; refund → 244A interest will arrive next year (taxable then).

## Interest (compute, don't estimate)

All use the assessed-tax base = total tax − TDS/TCS, with amounts **rounded down to the nearest ₹100**,
and months rounded UP (part month = full month).

- **234A** — late filing: 1%/month on unpaid tax from the day after the due date to filing date.
  Zero if filed on time OR no tax outstanding.
- **234B** — advance-tax shortfall: applies if advance tax paid < 90% of assessed tax.
  1%/month on the shortfall from 1 April of the AY to the month of payment. Emphasize to the user:
  this grows every month — quantify ₹/month to motivate paying now.
- **234C** — installment deferment, on the shortfall vs cumulative due at each date
  (15% by 15 Jun ×3mo, 45% by 15 Sep ×3mo, 75% by 15 Dec ×3mo, 100% by 15 Mar ×1mo), 1%/month.
  Relief: for dividend/CG arising during the year, liability arises only from the installment after
  receipt (this is why the return wants quarter-wise breakups). Skip 234C entirely if assessed tax is
  below the advance-tax threshold (₹10k — verify).
- **234F** — late-filing fee: flat (₹5,000; ₹1,000 if income ≤ ₹5L — verify).

Advance-tax exemptions: resident senior citizens (60+) with **no business income** owe no advance tax
→ no 234B/234C. AMT (115JC): only relevant for old-regime filers claiming specific business deductions
(10AA, 35AD, 80H–80RRB family) — if none apply, state so and move on; if they do, flag for CA review.

## Payment mechanics

- Pay via e-Pay Tax on the portal: **minor head 300 (self-assessment)** for return-time payment;
  minor head 100 for advance tax (before 31 Mar of the FY).
- After paying, the challan CIN (BSR code + date + serial) goes into Schedule IT so the return shows
  **zero balance payable at submission**. A return submitted with tax outstanding invites a 143(1) demand.
- Refund case: at least one bank account pre-validated on the portal, nominated for refund.
  If a refund fails (ECS bounce/name mismatch): re-validate the account and use the portal's
  "Refund Reissue" service. Outstanding prior demands get adjusted against refunds u/s **245** —
  the portal sends a notice first; respond within the window if the demand is wrong.

## After filing (what to tell the user to expect)

- **143(1) intimation**: automated match of the return vs department data — "no demand no refund" is
  the good outcome; a demand here usually means a TDS/AIS mismatch you should have caught in Phase 3.
- **139(9) defective-return notice**: fixable by responding within 15 days; common for missing
  balance-sheet fields in ITR-3 or TDS-claimed-without-income mismatches.
- **154 rectification**: for arithmetic/credit errors in the 143(1) processing — file online, no penalty.
- e-verification deadline is 30 days from submission; an unverified return = never filed.
