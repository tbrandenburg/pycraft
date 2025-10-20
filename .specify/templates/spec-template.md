# Feature Specification: [FEATURE NAME]

**Feature Branch**: `[###-feature-name]`  
**Created**: [DATE]  
**Status**: Draft  
**Input**: User description: "$ARGUMENTS"

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.
  
  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - [Brief Title] (Priority: P1)

[Describe this user journey in plain language]

**Why this priority**: [Explain the value and why it has this priority level]

**Independent Test**: [Describe how this can be tested independently - e.g., "Can be fully tested by [specific action] and delivers [specific value]"]

**CLI Contract**: Command `[cli command] [args]` → stdout (`[human readable output]`) | `--json` (`{...}`) | stderr on failure (`[message]`) | exit codes `[0, >0 mapping]`

**Library Touchpoints**: [`src/pycraft/module.py`: function → responsibility]

**Kid-Friendly Explanation**: [One-sentence story that a 12-year-old can repeat to explain the feature]

**Acceptance Scenarios**:

1. **Given** [initial state], **When** [action], **Then** [expected outcome]
2. **Given** [initial state], **When** [action], **Then** [expected outcome]

---

### User Story 2 - [Brief Title] (Priority: P2)

[Describe this user journey in plain language]

**Why this priority**: [Explain the value and why it has this priority level]

**Independent Test**: [Describe how this can be tested independently]

**CLI Contract**: Command `[cli command]` (`[args]`) | stdout (`[description]`) | `--json` schema snippet | stderr on failure (`[message]`) | exit codes mapping

**Library Touchpoints**: [`src/pycraft/...`: what changes]

**Kid-Friendly Explanation**: [Explain the change like teaching a friend in middle school]

**Acceptance Scenarios**:

1. **Given** [initial state], **When** [action], **Then** [expected outcome]

---

### User Story 3 - [Brief Title] (Priority: P3)

[Describe this user journey in plain language]

**Why this priority**: [Explain the value and why it has this priority level]

**Independent Test**: [Describe how this can be tested independently]

**CLI Contract**: Command `[cli command]` (`[args]`) | stdout (`[description]`) | `--json` schema snippet | stderr on failure (`[message]`) | exit codes mapping

**Library Touchpoints**: [`src/pycraft/...`: what changes]

**Kid-Friendly Explanation**: [Keep it simple and playful so a young learner understands]

**Acceptance Scenarios**:

1. **Given** [initial state], **When** [action], **Then** [expected outcome]

---

[Add more user stories as needed, each with an assigned priority]

### Edge Cases

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right edge cases.
-->

- What happens when [boundary condition]? (Include exit code and stderr expectations)
- How does system handle [error scenario]? (Describe logs surfaced with `--verbose`)

## Requirements *(mandatory)*

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right functional requirements.
-->

### Functional Requirements

- **FR-001**: Library module at `src/pycraft/[module].py` MUST expose [function/class] with documented inputs/outputs.
- **FR-002**: CLI command `[command]` MUST invoke the library module and respect the documented stdout/stderr contract.
- **FR-003**: Tests in `tests/unit/test_[module].py` MUST fail before implementation and pass afterward.
- **FR-004**: Integration/contract test in `tests/integration|contract/test_[feature].py` MUST cover user story acceptance.
- **FR-005**: Logging MUST emit structured key/value details and support `--verbose` toggling.
- **FR-006**: Repository MUST be managed with `uv` (`uv init`, `uv add`, `uv run`, `uv export --locked`) and document the commands in docs.
- **FR-007**: Source code MUST pass `uv run ruff check`, `uv run ruff format --check`, and include friendly comments that explain logic in plain language.

*Example of marking unclear requirements:*

- **FR-008**: System MUST authenticate users via [NEEDS CLARIFICATION: auth method not specified - email/password, SSO, OAuth?]
- **FR-009**: System MUST retain user data for [NEEDS CLARIFICATION: retention period not specified]

### Key Entities *(include if feature involves data)*

- **[Entity 1]**: [What it represents, key attributes without implementation]
- **[Entity 2]**: [What it represents, relationships to other entities]

## Success Criteria *(mandatory)*

<!--
  ACTION REQUIRED: Define measurable success criteria.
  These must be technology-agnostic and measurable.
-->

### Measurable Outcomes

- **SC-001**: [Measurable metric, e.g., "Users can complete account creation in under 2 minutes"]
- **SC-002**: [Measurable metric, e.g., "System handles 1000 concurrent users without degradation"]
- **SC-003**: [User satisfaction metric, e.g., "90% of users successfully complete primary task on first attempt"]
- **SC-004**: [Business metric, e.g., "Reduce support tickets related to [X] by 50%"]
- **SC-005**: [Learning metric, e.g., "A 12-year-old can retell the feature story after reading the comments"]
