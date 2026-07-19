# Contributing

This skill is prompt + reference markdown, not code — contributions are mostly **tax knowledge
and field reports**, and the bar is accuracy, not style.

## What's most valuable

1. **Field reports.** Ran the skill on a real return (yours!)? Open an issue with: profile shape
   (e.g. "salary + RSUs, ITR-2"), what worked, where it gave wrong/thin guidance. Redact all PII.
   This is the #1 need — most reference content is statute-derived and needs battle-testing.
2. **Annual refresh (~April–June).** Each new AY: new ITR utility schemas (schedule/field names in
   `references/10`), changed limits/rates flagged in the references, new portal validation quirks.
3. **Corrections with citations.** Tax content fixes must cite an official source (incometaxindia.gov.in
   Act/circular, or the e-filing portal). Secondary sources (ClearTax etc.) alone don't clear the bar.
4. **Depth in thin areas.** Currently thinnest: 44AE transporters, HUF/representative filings,
   property capital gains (54/54F exemptions), NR/RNOR returns.

## Ground rules

- **No PII ever** — no real PANs, names, account numbers, or actual return figures in issues, PRs,
  or examples. Use synthetic values.
- **Keep the numbers "shape, not truth".** The skill mandates runtime verification of every rate
  against official sources; hardcoded figures in references are illustrations. Don't add content that
  encourages trusting a written number over a verified one.
- **Respect the scope boundary**: this skill ends at the data-pack JSON. Portal automation / data
  entry belongs in a downstream agent, not here.
- **No aggressive-tax-position content.** Anything that over-claims exemptions or hides income gets
  rejected regardless of cleverness — see the red lines in SKILL.md.

## PR mechanics

Fork → branch → PR against `main`. For reference-file changes, say in the PR description which
official source backs the change. One topic per PR.
