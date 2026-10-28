# Public scope and evidence

Terms and acronyms are defined in the [glossary](03-glossary.md).

The public specification defines dimensions, public criteria, score architecture, evidence categories and interpretation principles. It supports review of what is assessed and how findings should be understood.

Detailed response rubrics, calibration, point thresholds within criteria, verification rules and algorithms remain outside this repository. MYCOBI limits disclosure to protect its implementation and reduce opportunities to optimize reported answers without improving the underlying company condition. This is a design rationale, not a demonstrated anti-gaming result.

## Evidence categories

| Category | Examples | Public interpretation |
| --- | --- | --- |
| Structured self-report | Diagnostic responses and descriptions | Records what the company asserts. |
| Documentary records | Financial statements, agreements, filings, certificates | May support or contradict a claim; origin and scope matter. |
| Operational system records | Accounting, banking, billing, payroll, CRM, capitalization records | Can help corroborate claims; a system connection does not itself prove accuracy. |
| Cross-checks | Comparisons between claims and records | Can reveal inconsistencies requiring explanation. |

The public specification does not assign points, acceptance thresholds or confidence weights to these categories. Field reviewers MUST NOT invent those rules or represent a worksheet as an official scored assessment.

## What an assessment explanation should preserve

A useful explanation SHOULD identify the criterion, the material weakness, evidence categories considered, relevant limitations and unresolved inconsistencies. It need not disclose private detection logic or exact point calculations.

Missing evidence, contradictory evidence and an observed weakness are different findings. Reviewers SHOULD preserve that distinction instead of silently treating them as equivalent. This document does not prescribe their numerical effects.

## Public analogy and limits

FICO publishes broad factor categories and general relative importance. VantageScore explains factors and reason codes while describing calculation rules as proprietary. These support separating public interpretation from a private model. They do not establish that IRS has equivalent predictive validity.

- https://www.myfico.com/credit-education/whats-in-your-credit-score
- https://www.vantagescore.com/consumers/consumer-faqs
- https://vantagescore.com/resources/faqs
- https://www.fdic.gov/resources/regulations/federal-register-publications/2006/06c03ac96.pdf

The 2006 VantageScore submission describes its original score range and intended risk outcome. It is not evidence that all present disclosure practices existed at launch.

## Comparability and validation

The public specification alone cannot reproduce a MYCOBI IRS. Independently developed scoring models MUST NOT be described as interchangeable solely because they use the same criteria or numerical range.

Validation results and limitations SHOULD be published as evidence becomes available. No prediction of financing success, reduction in investment risk or equivalence to a credit rating is established by this draft.
