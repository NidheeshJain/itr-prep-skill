# Phase 4 — Capital Gains (Schedule CG)

**Rates and holding periods changed materially in July 2024 and can change again — verify current-AY
rates online before computing.** The bucket structure below is stable; the numbers are not.

## Asset buckets

| Asset | ST if held ≤ | ST rate | LT rate | Notes |
|---|---|---|---|---|
| Listed equity shares / equity MF / equity ETF (STT paid) | 12 mo | 111A special rate (verify, ~20%) | 112A special rate (verify, ~12.5%) above annual exemption (verify, ~₹1.25L) | grandfathering (FMV 31-Jan-2018) for pre-2018 buys |
| Debt MF bought ≥ 1-Apr-2023 | always deemed ST | slab | — | Sec 50AA; no LTCG ever |
| Debt MF bought earlier / other non-equity funds (silver/gold ETF etc.) | 24 mo (verify) | slab | 112 rate (verify) | classification of hybrid/international funds changes — check fund's equity % |
| Property / land | 24 mo | slab | 12.5% no-indexation, with legacy 20%-indexed option for pre-Jul-2024 buys (verify) | stamp-duty value substitution 50C; TDS 194-IA |
| Gold (physical), unlisted shares, other assets | 24 mo | slab | 112 rate (verify) | |
| **Crypto/VDA** | n/a | **flat 30% u/s 115BBH** | same | NO loss set-off (not even VDA-vs-VDA), no expense deduction except cost, 1% TDS 194S; separate Schedule VDA |

VDA extras: Schedule VDA wants **one line per transfer** (acquisition date, transfer date, cost,
consideration); no 87A rebate and no basic-exemption benefit against VDA income — 30% from the first
rupee, in both regimes; gifted crypto is taxable to the recipient u/s 56(2)(x) above the threshold;
investor → capital-gains head, habitual trader → business head (schedule splits accordingly).
Any VDA transfer bars ITR-1/4.

## Computation rules

- Full value of consideration − (cost of acquisition + improvement + **transfer expenses**).
  Transfer expenses include brokerage on sale and **DP charges on the sale** (small but legitimate) —
  but NOT STT (STT is never deductible in CG; it IS deductible in F&O business income — see ref 05).
- Buyback of listed shares (post Oct-2024 rule): proceeds taxed as **dividend** in Other Sources,
  cost becomes a capital loss — verify current treatment.
- Corporate actions: splits/bonus adjust cost basis (bonus shares = 0 cost, holding from allotment).
- Quarter-wise breakup of gains is required in the return (for 234C) — get sale dates from the
  tradewise/scripwise sheet.

### Scripwise 112A detail (feeds `csv_ready_112A`)

- ITR requires scripwise reporting for 112A (ISIN, name, cost, sale) — the broker Tax P&L has it.
- Capture scripwise rows **per unit** (sale price, cost, FMV each ÷ quantity) with raw acquisition and
  transfer dates, into the data pack's `csv_ready_112A` block (reference 10): the portal's 112A screen
  takes a CSV upload built from its own downloadable template, and per-unit values + both dates are
  what every template revision asks for. The filling agent maps these into the current AY's template;
  it falls back to the broker tax report for anything missing.
- **Grandfathering formula** (pre-31-Jan-2018 holdings): deemed cost = higher of (actual cost,
  lower of (FMV on 31-Jan-2018, sale price)). Apply it when computing the gain in Phase 4 — don't
  take FMV as cost outright: when FMV exceeds the sale price, the deemed cost is capped at sale
  price (gain 0, not a manufactured loss). The portal template auto-computes this from raw inputs.
- **FMV source**: broker/CAMS-KFintech tax reports usually carry the grandfathered value; if absent,
  use the scrip's highest traded price on 31-Jan-2018 (NSE/BSE) or the fund's NAV on that date
  (AMFI), and record the per-scrip source in the pack.
- **112A eligibility isn't automatic**: shares need STT on acquisition AND sale (equity MF: sale
  only) — but gifts, off-market transfers, IPO/bonus/rights/ESOP allotments are carved out by
  notification (verify). A holding acquired without STT and outside the carve-outs falls under
  **Sec 112, not 112A** — different rate, no ₹1.25L exemption.
- **Missing acquisition dates** (demat transfers-in, gifts, opening balances): the broker report
  often lacks them, so the fallback fails too — mark the row VERIFY and get the date/cost from
  contract notes, the previous broker, or the CAS. Without the date you can't even set the
  acquisition-cliff code.

## Property LTCG exemptions (Sec 54 family) — verify current rules before relying

- **54**: LTCG on a residential house, reinvested in another house (buy within 2 yrs / construct
  within 3 yrs; purchases up to 1 yr before sale count). **54F**: LT gain on any non-house asset,
  invest the full consideration in one house (proportionate exemption otherwise; barred if holding
  more than one other house). **54EC**: gains into notified bonds within 6 months, ₹50L cap, 5-yr lock-in.
- 54 and 54F exemptions are capped (₹10 Cr of reinvestment since 2023 — verify) — only bites on
  large gains, but check before promising full exemption.
- Not reinvested by the return due date? Park the amount in a **Capital Gains Account Scheme (CGAS)**
  deposit before filing to preserve the claim — a routinely missed deadline.
- These claims need detail rows in ITR-2/3 (dates, amounts, CGAS refs) — collect the documents up front.

## Set-off inside CG (before anything leaves the schedule)

- STCL sets off against any CG (ST or LT). LTCL sets off ONLY against LTCG.
- Equity STCL can absorb non-equity STCG and vice versa — buckets differ in RATE, not in set-off.
- Exempt-threshold interaction: the 112A annual exemption applies AFTER loss set-off.
- Net loss → Schedule CFL, 8-year carry-forward, **only if filed by due date**.

## Stale rates can hide inside otherwise-official documents

A rate or threshold pulled from an extracted form PDF is not automatically current just because the
PDF looks official — instruction paragraphs and boilerplate sometimes carry over unchanged from a
prior AY's version even in an otherwise-current document (112A's rate/exemption has been a repeat
source of this confusion). Corroborate a suspicious-looking rate — especially one that matches what
you'd expect from last year — against a second, independent official source (e.g. the AY's
validation-rules document, not just the form text) before using it in a computation.

## AIS cross-check

AIS SFT section lists each securities sale with consideration and cost. Match scrip-level against the
broker statement. AIS cost basis is sometimes wrong (especially for transfers between demats or IPO
allotments) — the broker/actual records win, but note the mismatch for a possible AIS feedback response.
