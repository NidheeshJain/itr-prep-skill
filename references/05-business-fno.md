# Phase 4 — Business, Profession, F&O (Schedules BP / P&L / BS, ITR-3/4)

## Classification first

| Activity | Head | Type |
|---|---|---|
| F&O (index/stock/currency/commodity derivatives) | Business | **Non-speculative** |
| Intraday equity (no delivery) | Business | **Speculative** (separate pool — its loss only offsets speculative profit) |
| Delivery-based equity/MF | Capital gains (unless the user genuinely trades as a business at scale — rare, ask only if volumes are huge) |
| Freelance/consulting/professional fees | Business/Profession (44ADA presumptive often available) |
| Commission/agency | Business (44AD NOT available for commission income) |

## F&O turnover (for the audit check)

ICAI method: sum of **absolute** profits and losses per trade; for options add premium received on sale
only where not already included in the P&L. Broker Tax P&L statements state turnover on this basis —
use their figure. Turnover is NOT contract value; users panic over crores of contract value when actual
turnover is in thousands.

## Tax audit (44AB) decision

- Turnover ≤ ₹1 Cr → no audit. ₹1–10 Cr → no audit if ≥95% of transactions are digital (broker trades
  always are). > ₹10 Cr → audit. (Verify current thresholds.)
- **44AD trap**: if the user opted for presumptive 44AD in any of the past 5 years and now declares
  profit below the presumptive rate (or a loss) while income exceeds the basic exemption → audit
  required regardless of turnover [44AD(4)+(5)]. Ask about prior-year presumptive filings explicitly.
- Audit ⇒ CA required, different due date (usually 31 Oct), Form 3CD. Out of scope for self-filing —
  hand off to a CA and say so plainly.

## Presumptive schemes (ITR-4 territory)

- **44AD** (business): declare ≥6% (digital receipts) / 8% (cash) of turnover; limit ₹2 Cr (₹3 Cr if
  ≥95% digital — verify). Opting out after use triggers the 5-year lock-out above.
- **44ADA** (professions u/s 44AA: IT, consulting, medicine, law…): declare ≥50% of gross receipts;
  limit ₹50L (₹75L if ≥95% digital — verify). Creator/influencer income has a dedicated
  **profession** code (16021 "Social media influencers") that appears only under the 44ADA dropdown —
  don't misclassify it as a 44AD business just because 6% < 50%; pick the section that legally fits.
  Presumptive filers must supply the no-books block figures (Part A-BS item 6: debtors, creditors,
  stock, cash balance — a positive cash balance, e.g. retained net profit, with the rest 0 is fine);
  include them in the data pack, since the portal blocks upload if the block is empty.
- Presumptive = no books, no expense tracking, but you CANNOT declare a loss under it. A loss-making
  F&O trader should use normal provisions (ITR-3), not presumptive.

## Expenses (normal provisions)

Deductible against F&O/trading business income:
- Direct: brokerage, exchange transaction charges, **STT** (deductible here, unlike in CG), SEBI fees,
  stamp duty, GST on charges, clearing charges, IPFT.
- Account-level (allocate reasonably): DP/pledge/delayed-payment charges, DDPI/platform fees.
- Indirect (only if real and documented): internet, data subscriptions, advisory fees, depreciation on
  computer/phone proportionate to trading use. Warn: keep proofs; don't invent round numbers.
- DP charges on **delivery sales** belong to capital gains (transfer cost), not here.

## Books and the "No Account Case"

For small F&O turnover, the broker Tax P&L is adequate; use the no-account-case fields
(gross receipts, gross profit, expenses, net profit) in Part A-P&L rather than fabricating a balance
sheet. Enter turnover and net P&L in the Trading Account section where the utility requires it.
Nature-of-business code: securities/derivatives trading (financial intermediation family — pick from
the utility's current code list, e.g. 09028-type codes; codes shift between years).

## Where the numbers land

- Non-speculative net profit/loss → Schedule BP main computation.
- Speculative (intraday) net → separate speculative rows in BP.
- Business loss set-off/carry-forward rules → reference 07 (critically: it MUST set off against other
  heads this year where permitted — it cannot be voluntarily preserved for carry-forward).
