# Phase 4 — Salary

## Assembly

Sum across ALL employers in the FY: 17(1) salary + 17(2) perquisites (RSU/ESOP vesting value lives here,
from Form 12BA) + 17(3) profits-in-lieu. Then subtract Sec 10 exemptions, then Sec 16 deductions.
Report each employer separately in Schedule S (TAN + name + gross), but exemptions/deductions apply
to the year as a whole.

## Multi-employer traps (the highest-value checks in the whole skill)

1. **Standard deduction is ONCE per year**, not per employer. Each Form 16 grants its own — the return
   must apply a single one (new-regime and old-regime amounts differ; verify current values).
2. **Slabs got applied twice.** Each employer taxed its own salary from ₹0 up, so combined TDS is almost
   always short. Expect a balance payable; tell the user early so it isn't a shock.
3. **Mixed regimes across employers.** Form 16s may disagree on 115BAC opt-out. The return is ONE regime
   for the whole year: rebuild both salaries under the chosen regime —
   - drop old-regime-only items an employer applied (professional tax u/s 16(iii), 80C, HRA exemption)
     if filing new regime;
   - retain regime-agnostic exemptions (see below) in either regime.
4. **Employment-period overlap**: if AIS "Other information" shows overlapping employment dates, ask —
   dual salary in the same month is legitimate (notice-period overlap) but changes nothing except totals.

## Sec 10 exemptions — which survive the new regime

| Exemption | Old regime | New regime | Notes |
|---|---|---|---|
| HRA 10(13A) | ✔ | ✘ | least of: actual HRA / rent−10% of basic / 50% (metro) or 40% of basic |
| LTA 10(5) | ✔ | ✘ | |
| Leave encashment 10(10AA) | ✔ | ✔ | on resignation/retirement; see formula below |
| Gratuity 10(10) | ✔ | ✔ | non-govt: least of actual / ₹20L / 15 days' salary per year of service |
| Retrenchment/VRS 10(10B)/10(10C) | ✔ | ✔ | |
| Employer NPS 80CCD(2) | ✔ | ✔ | technically Chapter VI-A but survives new regime; % of basic cap differs by regime — verify |

### Leave encashment 10(10AA) — least of four (non-government)
1. Amount actually received;
2. Lifetime ceiling (₹25L currently — verify; it's a LIFETIME pool across employers, tell the user usage reduces future headroom);
3. 10 × average monthly salary;
4. Unavailed leave (capped at 30 days per completed year of service) × average daily salary.

"Salary" here = **basic + DA + fixed-commission only** — never HRA/special allowance, in BOTH regimes.
"Average" = last 10 months before exit. Users routinely ask why the exempt figure is far below what they
were paid: the employer often pays on a wider base/more days than the statute shields. The employer's
Form 16 figure is usually right; sanity-check it against the formula (per-day basic × leave-day balance —
ask the user their approximate leave balance at exit) rather than recomputing to the rupee.
If the user wants to claim the full amount received: refuse and explain (see SKILL.md red lines).

## Sec 16

- Standard deduction: once, current-year amount per regime (verify online).
- Professional tax 16(iii): old regime only.
- Entertainment allowance: govt employees, old regime only.

## Common perquisite/pay items and where they go

| Item | Treatment |
|---|---|
| Joining bonus / retention bonus | 17(1) salary, fully taxable when received |
| Bonus clawback/repayment | grey area — flag for CA advice if material |
| RSU/ESOP vest (listed foreign parent) | 17(2) perquisite at vest (in Form 16/12BA); ALSO triggers Schedule FA (ref 09); sale later = capital gains |
| Notice-pay recovery | usually taxable on gross (deduction contested); flag if material |
| Arrears | taxable now; Sec 89 relief via Form 10E possible — compute if material |
| PF withdrawal <5 yrs service | taxable + TDS 192A; appears in AIS |
