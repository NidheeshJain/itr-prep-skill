# Phase 5 — Loss Set-off, Carry-forward, Regime Comparison (CYLA / BFLA / CFL)

## Order of operations (mandatory, not optional)

1. **Intra-head** (Sec 70): losses first absorb income within the same head/sub-pool.
2. **Inter-head, same year** (Sec 71, Schedule CYLA): remaining losses set off against other heads,
   subject to the restrictions below. **This is compulsory** — a loss that CAN be set off this year
   MUST be; you cannot park it for carry-forward because a future set-off would be worth more.
3. **Brought-forward** (Schedule BFLA): prior-year losses absorb what remains, oldest first,
   same-head-only rules apply.
4. **Carry forward what survives** (Schedule CFL) — only if the return is filed by the 139(1) due date
   (exceptions: HP loss and unabsorbed depreciation survive late filing).

## Set-off restriction matrix

| Loss | Can set off against (same year) | Carry fwd | Future set-off against |
|---|---|---|---|
| Non-speculative business (incl. F&O) | any head EXCEPT salary [71(2A)] | 8 yrs | any business income (incl. speculative) |
| Speculative business (intraday) | speculative profit ONLY | 4 yrs | speculative only |
| STCL | STCG + LTCG only | 8 yrs | STCG + LTCG |
| LTCL | LTCG only | 8 yrs | LTCG only |
| House property | other heads up to ₹2L (old regime); **nil inter-head in new regime** | 8 yrs | HP income only |
| Other sources (non-race-horse) | cannot be carried; set off in year | — | — |
| VDA/crypto | nothing, ever | none | none |

Consequence worth stating to users: an F&O loss smaller than their interest/dividend income will be
fully consumed THIS year (good — instant 30%-slab relief) and nothing carries forward. Don't promise
a carry-forward before running CYLA.

## Regime comparison (do it with real numbers)

Compute total income and tax under BOTH regimes:
- Old: apply HRA/LTA, all Chapter VI-A, HP-loss inter-head set-off, old slabs + old rebate.
- New: default slabs, higher standard deduction, only surviving exemptions (10(10AA), gratuity,
  80CCD(2)), no HP inter-head loss.
- Same in both: special-rate CG, VDA, lottery; business loss mechanics (mostly), carry-forwards.
Present a two-column table ending in final tax payable, and recommend the lower — with the caveats:
business-income filers locking regime via 10-IEA; salaried can re-choose next year freely.

## Prior-year losses

Pull Schedule CFL from last year's **filed ITR JSON** (how to obtain/parse: reference 02). Verify each
vintage's remaining life (8/4 years from the loss year) and that the originating return was on time.
Enter year-wise rows in CFL — the utility wants per-AY breakdown, not a lump sum.

- **Unabsorbed depreciation (Schedule UD)** is separate from business loss: no expiry, survives belated
  filing, and sets off against any head except salary. Don't merge it into the business-loss rows.
- Brought-forward losses only set off within their own head rules (BFLA) — e.g. b/f STCL needs current
  CG income; b/f business loss needs current business income. If nothing absorbs them this year, they
  roll forward with one less year of life — show the updated vintage table in the data pack.
- If a prior 143(1) intimation adjusted the loss figures, the intimation's numbers govern, not the
  as-filed return.
