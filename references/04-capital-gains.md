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
- ITR requires scripwise reporting for 112A (ISIN, name, cost, sale) — the broker Tax P&L has it.

## Set-off inside CG (before anything leaves the schedule)

- STCL sets off against any CG (ST or LT). LTCL sets off ONLY against LTCG.
- Equity STCL can absorb non-equity STCG and vice versa — buckets differ in RATE, not in set-off.
- Exempt-threshold interaction: the 112A annual exemption applies AFTER loss set-off.
- Net loss → Schedule CFL, 8-year carry-forward, **only if filed by due date**.

## AIS cross-check

AIS SFT section lists each securities sale with consideration and cost. Match scrip-level against the
broker statement. AIS cost basis is sometimes wrong (especially for transfers between demats or IPO
allotments) — the broker/actual records win, but note the mismatch for a possible AIS feedback response.
