# Investment Readiness Methodology

**Status:** Draft  
**Version:** 0.1.0-draft

Terms and acronyms are defined in the [glossary](03-glossary.md).

## 1. Core principle

A low readiness score is an actionable development map, not a permanent verdict. The purpose of Investment Readiness is to surface structural diligence gaps and help teams close them before investor meetings.

## 2. Relationship to technical and commercial maturity

Technical maturity and commercial maturity are separate questions from the one this standard addresses. Investment Readiness asks whether corporate fundamentals are aligned with institutional capital requirements. This standard does **not** define a formula that rolls technical or commercial maturity into the Investment Readiness Score, and strength in either area does not offset gaps in investment readiness.

## 3. The 0–1000 Investment Readiness Score (IRS)

The Investment Readiness Diagnostic (IRD) produces an Investment Readiness Score (IRS) from 0 to 1000. Comparability depends on assessment context and model version; shared numerical ranges alone do not establish equivalence.

Two evaluation layers inform interpretation:

1. **Demonstration:** Structured claims across the 25 criteria.
2. **Validation:** How strongly those claims are supported by documents and/or connected business systems.

The public specification distinguishes claims from their supporting evidence. It does not disclose how evidence affects point calculations, confidence measures or verification outcomes. See [public scope and evidence](04-public-scope-and-evidence.md).

## 4. Five scoring dimensions

The IRS is built from five equal structural dimensions. Each contributes up to **200 points** toward the 1,000-point total.

| Dimension | Code | Point range | What investors are testing |
| --- | :---: | :---: | --- |
| Financial Health | FH | 0–200 | Accounting rigor, revenue trend, cash burn and runway, unit economics, forecast discipline |
| Operational Maturity | OM | 0–200 | Leadership completeness, key-person risk, operating cadence, product infrastructure, key performance indicator (KPI) management |
| Market Position | MP | 0–200 | Ideal customer profile (ICP) clarity, product-market fit proof, competitive moat, go-to-market execution, realistic market headroom |
| Governance & Compliance | GC | 0–200 | Entity structure, intellectual property (IP) assignment, cap-table hygiene, regulatory posture, risk/insurance controls |
| Traction | TR | 0–200 | Revenue velocity, retention and cohort health, pilot conversion, partnerships, market momentum |

Institutional diligence does not treat one pillar as optional. Balance across dimensions matters as much as the headline total.

## 5. Twenty-five criteria

The score is assembled from **25 criteria** (five per dimension). Criteria evaluate infrastructure maturity and auditable proof, not binary checklist declarations.

The normative names and measurement scopes live in [02-criteria-index.md](02-criteria-index.md).

## 6. Evidence categories

Evidence may include:

1. **Structured baseline:** Self-reported diagnostic inputs
2. **Documentary artifacts:** Financials, cap tables, IP assignments, insurance certificates, contracts, and similar records
3. **System records:** Banking, accounting, billing, customer relationship management (CRM), payroll, or cap-table system outputs that corroborate claims
4. **Cross-checks:** Comparing claims against documents or system records to surface inconsistencies

Self-report and corroborated records are distinct evidence categories. Their numerical treatment is not specified publicly.

**Why provenance matters.** Readiness frameworks commonly require substantial evidence, but the evidence is usually authored by the company being assessed. The effort of assembling it is similar whether the company's condition is strong or weak, so the result is hard to distinguish from outside. Records the company does not author, such as banking, accounting, billing and cap-table system records, behave differently: a company either has the history or it does not. This standard therefore treats the source of evidence as distinct from its volume, and treats cross-checks between claims and such records as a way to show the distance between what is asserted and what is documented. A system connection alone does not establish independence or accuracy. The public specification does not state how provenance affects any score.

## 7. Stage-relative scoring

**Open decision:** The existing approach below requires confirmation of whether stage changes scoring expectations or only interpretation. See D-08 in [open decisions](../OPEN-DECISIONS.md).

Readiness is evaluated relative to a declared funding stage (Pre-Seed, Seed, Series A, Series B+).

An early Pre-Seed company with little or no commercial revenue can still earn a strong IRS when Financial Health and Governance reflect infrastructure quality (formation, banking, cap-table integrity, basic reporting), not absolute annual recurring revenue (ARR). Expectations scale with stage:

| Stage | What “strong” typically emphasizes |
| --- | --- |
| Pre-Seed | Corporate hygiene, IP assignment, founder/team clarity, early customer discovery, basic financial controls |
| Seed | Early unit-economic signals, documented pipeline or first revenue, monthly accounting discipline, tightening governance |
| Series A | Repeatable acquisition or retention proof, stronger financial controls and forecasts, formal governance cadence, scalable operations |
| Series B+ | Institutional-grade reporting, multi-channel retention and growth evidence, mature controls, diligence-ready documentation posture |

This standard does **not** publish a fixed score-to-round-size ladder. Capital-market round sizes and investor expectations change over time.

## 8. Score bands

| IRS range | Public label |
| --- | --- |
| 800-1000 | Pending steward decision |
| 600-799 | Pending steward decision |
| 400-599 | Pending steward decision |
| 200-399 | Pending steward decision |
| 0-199 | Pending steward decision |

The five ranges are proposed guidance for assessed investment readiness, not funding-round assignments. Labels remain open for review. A higher band does not establish low investment risk, funding eligibility or particular terms.

The aggregate score must be read with dimension findings, evidence categories and material limitations. Stage provides context; a strong pre-seed assessment does not establish preparation for public-market diligence.

## 9. Limitations

The 25 criteria and five dimensions rest on expert judgment about the diligence domains investors review. Their coverage has not been established by formal psychometric procedure and should be read as a structured proposal. The predictive validity of the IRS is not established: linking scores to later diligence results, financing events and survival requires longitudinal data that does not yet exist. Comparability across sectors and company types is also unresolved. Stage-relative interpretation addresses part of it but not all. Early-stage companies often have few records to corroborate, so their assessments rest on weaker evidence and should be read accordingly. The score locates areas for development. It is not a pass or fail gate, does not guarantee funding or any outcome, and does not map to a financing round or a round size.

## 10. FAQ

### What is the maximum score?

1000.

### Does the IRS measure technology or business maturity?

No. It addresses investment readiness only. Other maturity measures answer different questions.

### Why is there no published score-to-funding-amount table?

Round sizes and investor expectations shift. This specification focuses on a durable measurement vocabulary.

### How do I propose a change?

See [../CONTRIBUTING.md](../CONTRIBUTING.md) and [../rfcs/0000-template.md](../rfcs/0000-template.md).
