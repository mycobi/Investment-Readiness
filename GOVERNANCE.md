# Governance

## Steward

MYCOBI, Inc. stewards the Investment Readiness standard while it is in formation. Stewardship means:

- Maintaining this repository and release tags
- Accepting or deferring RFCs
- Keeping the public ontology coherent
- Inviting industry feedback

Stewardship is not exclusive ownership of the *idea* of investment readiness. The specification is published so others can adopt and improve it under the license terms.

## Roles

| Role | Responsibility |
| --- | --- |
| **Maintainer** | Merge editorial PRs; accept/defer RFCs; cut draft/release tags |
| **Contributor** | Open issues, discussions, RFCs, and pull requests. People outside MYCOBI use a fork. |
| **Adopter** | Uses the vocabulary in programs, teaching, or tools; feedback welcome |

People outside MYCOBI do not have write access. They fork the repository and open a pull request. MYCOBI maintainers may commit directly. Only MYCOBI maintainers merge. Maintainer GitHub accounts for code ownership are listed in [.github/CODEOWNERS](.github/CODEOWNERS). A GitHub team may replace those accounts later. The same accounts are the designated reviewers described below.

## Proposal states (RFCs)

| State | Meaning |
| --- | --- |
| Draft | Authoring in progress |
| Under Review | Open for comment |
| Accepted | Will be merged into the normative docs |
| Deferred | Not now; may revisit |
| Rejected | Will not proceed (with short rationale) |

## Releases

- **Draft tags** (`v0.x.x-draft`): incubation; breaking changes allowed with notice
- **Release candidates** (`v1.0.0-rc.N`): intended stable surface
- **Normative releases** (`v1.0.0+`): breaking changes require an Accepted RFC and a migration note

## Conflict resolution

If contributors disagree, maintainers decide after discussion. Decisions and rationales should be recorded on the RFC or Issue.

## Acceptance and review gates

Follow CONTRIBUTING.md and MAINTAINER-REVIEW.md for every incorporated contribution. Each PR requires explicit acceptance records and approval by an authorized reviewer other than its author. Silence is never signature or material-change approval. License and CLA changes also require steward approval.

For the review window, MYCOBI designates @andry3ag and @scott-mycobi as reviewers. A PR authored by one of them is approved by the other; a PR from anyone else may be approved by either. MYCOBI may add reviewers, including outside practitioners, and records any change in OPEN-DECISIONS.md.

Each release records a version, date, accepted RFCs and change summary. Preserve earlier releases and agreement versions. Later CLA edits do not alter earlier acceptance.

The research paper remains separately authored and versioned. A methodology change arising from paper feedback follows this process.

## Review window and decisions

The confirmed review window runs from 28 October 2026 to 28 April 2027. The phase dates and monthly digests in ROADMAP.md follow that window. The first digest is 28 November 2026.

Confirmed service target: acknowledge substantive submissions within five business days during the review window. Acknowledgment identifies the review route and next step; it does not promise technical resolution within five days. For this process, count Monday through Friday beginning the next weekday after receipt, using America/New_York dates. No unpublished holiday exclusions apply. A maintainer MUST record missed targets and provide a next review date. An automated receipt alone does not satisfy substantive acknowledgment.

Consensus means the maintainer has considered substantive objections and documented why the resulting proposal is acceptable. Vote counts and silence alone do not establish consensus. A concern may identify ambiguity, missing evidence, inconsistency or operational harm; contributors need not prove realized harm or supply replacement prose to be heard.

Record substantive decisions in DISPOSITION-OF-COMMENTS.md with the concern, outcome, rationale, reviewer and resulting change. Preserve unresolved objections and explain deferrals. MYCOBI retains final stewardship authority while the standard is in formation. Ratification here is a MYCOBI release decision, not approval by an external standards organization.

Individual CLA acceptance follows CONTRIBUTOR-ACCEPTANCE.md. Reviewers must still check all original authors and any entity or employer-authority exceptions.
