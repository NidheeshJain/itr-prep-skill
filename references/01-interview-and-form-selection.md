# Phase 1 — Interview and Form Selection

## Scope: assessee type

This skill's workflows assume an **Individual** filer. If the return is for an HUF, a deceased person
(legal-heir filing), a minor (income not clubbed), or any representative-assessee case, say so upfront:
the same heads/schedules largely apply but registration steps, slab nuances, and verification differ —
handle with extra care and recommend a CA for the first such filing.

## The interview

Batch these into 2–3 AskUserQuestion rounds. Round 1 (always):

1. **Income sources this FY** (multi-select): Salary / Sold shares-MF-crypto / F&O or intraday trading /
   Business or freelance income / Rent received / Interest & dividends / Pension / Agriculture / None of these extra.
2. **Job changes**: same employer all year / changed jobs / multiple simultaneous employers / not salaried.
   (Job change = the single most common cause of tax shortfall — each employer applies slabs independently.)
3. **What they want**: full filing help / just form+regime / compute tax / verify a drafted return / prep checklist.

**Age — derive, don't ask.** DOB matters (60+/80+ changes old-regime slabs, 80TTB, 80D limits, and the
advance-tax exemption for seniors with no business income), but get it from documents during Phase 2:
AIS Part A (General Information) states DOB, and the AIS decryption step already required the user to
supply it — reuse that. Only ask the user directly if, after document collection, no DOB-bearing
source is available (e.g., they provided only Form 16s and broker statements, which don't carry DOB).

Round 2 (conditional on round 1):

4. **Residency** (only if any hint of foreign ties, NRI status, or >182-day absence): days in India this FY
   and the 4 preceding FYs. Determine ROR / RNOR / NR per Sec 6 — verify current thresholds online
   (60-day rule variants, deemed-residency for high-income citizens).
5. **Foreign** (ask everyone ONCE, plainly): "Do you have any foreign bank account, foreign stocks
   (including US RSUs/ESPPs via your employer), or foreign income?" — a yes forces ITR-2/3 + Schedule FA.
6. **Prior-year losses**: "Did any earlier return carry forward losses (shares, F&O, property)?" If unsure,
   check last year's ITR acknowledgment/computation.
7. **Disqualifier sweep** (yes/no list): company director? unlisted/startup shares (incl. ESOPs of private
   companies)? more than one house property? agricultural income above ₹5,000? TDS deducted under 194N
   (large cash withdrawals)? income clubbed from spouse/minor?

## Form decision tree

Apply in order; first match wins. Verify current-year eligibility tweaks online (the CBDT adjusts these —
e.g., small LTCG was allowed into ITR-1/4 from AY 2025-26).

| Condition | Form |
|---|---|
| ANY business/profession income: F&O, intraday, freelance, consulting, commission, presumptive | **ITR-3** (or **ITR-4** if presumptive-only and eligible) |
| Presumptive only (44AD/44ADA/44AE), resident, total income ≤ ₹50L, no CG beyond permitted small LTCG, no foreign, ≤1 house property | **ITR-4** |
| Capital gains (beyond ITR-1-permitted sliver), >1 house property, foreign assets/income, director, unlisted shares, RNOR/NR, clubbed income, carried-forward losses | **ITR-2** |
| Resident individual, income ≤ ₹50L, salary/pension + 1 house property + other sources, agri ≤ ₹5,000 | **ITR-1** |

Key traps:
- **Any F&O trade, even one, even a loss → business income → ITR-3.** Intraday equity = *speculative*
  business (separate from F&O's *non-speculative*). Delivery-based selling = capital gains, not business.
- **Foreign RSUs from an Indian employer of a foreign parent → Schedule FA → minimum ITR-2**, even if
  the user never sold anything. Holding is reportable, not just selling.
- **Director or unlisted shares → ITR-1/4 barred** regardless of income size.
- Carried-forward losses to claim or new losses to carry → ITR-1 barred (it has no CFL schedule).

## Provisional regime call

Don't finalize until Phase 5, but set expectations early:
- New regime is the **default**. Old regime requires opting out — and for business-income filers that
  means **Form 10-IEA before the due date**, and the choice is near-one-shot (one switch-back allowed).
  Salaried-only filers can flip regime each year inside the return itself.
- Quick heuristic: old regime needs roughly ₹4L+ of genuine deductions (HRA + 80C + 80D + home-loan
  interest…) to beat new at mid incomes — verify with the real side-by-side in Phase 5, never assert
  from the heuristic alone.
- The **employer's regime choice on Form 16 does not bind the return.** The filer re-decides for the
  whole year. Two employers may even have used different regimes — the return rebuilds everything
  under one.

## Filing-section basics

- On time (139(1)) → all carry-forwards preserved.
- Belated (139(4), usually until 31 Dec) → 234F fee, 234A interest, **loss carry-forwards forfeited**
  (except house-property loss and unabsorbed depreciation).
- Revised (139(5)) → can fix an already-filed return until 31 Dec; carry-forwards survive if the
  original was on time.
- Updated (139(8A), ITR-U) → up to 4 years late but with additional tax (25–70%); last resort only.
