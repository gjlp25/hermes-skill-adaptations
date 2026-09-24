---
name: internal-comms
description: Draft a structured internal team communication from facts.
version: 0.1.0
author: Anthropic (upstream), Robert (gjlp25), Hermes Agent
license: Apache-2.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [internal, communications, status, incident]
    related_skills: []
---

# Internal Communications Skill

Draft an internal-facing update from facts the user provides, with the format chosen for a specific audience. This is not a substitute for company policy, legal review, or incident command.

## When to Use

- A user requests a 3P update, status report, leadership update, internal newsletter, FAQ, project update, or incident summary.
- The intended audience is internal to an organization or team.
- Do not use for public announcements, marketing copy, external press statements, or communications that require unprovided confidential facts.

## Prerequisites

- Identify the audience, communication type, owner, and publication channel.
- Use only facts supplied in the active conversation or approved task material.
- Ask for missing material facts rather than inventing status, dates, commitments, metrics, or root causes.

## Procedure

1. Select the format: 3P, status, leadership, newsletter, FAQ, project update, or incident summary. Completion: the draft has a named format and audience.
2. Separate confirmed facts from open questions and assumptions. Completion: unconfirmed items are labelled or omitted.
3. Draft the message with a direct title, current state, decisions or progress, risks or blockers, and requested action where relevant. Completion: each section is relevant to the selected format.
4. For an incident summary, include impact, known timeline, current mitigation, and next update time only when supplied. Completion: the draft does not speculate about cause or blame.
5. Present the draft for the user's review before any publication action. Completion: no external message is sent by this skill.

## Quick Reference

- 3P: Progress / Plans / Problems.
- Status: Summary / completed / next / risks / asks.
- Leadership: outcome / decision needed / metrics provided / risk / owner.
- Incident: impact / timeline / mitigation / next update.

## Security and Privacy

Treat internal facts as confidential. Do not retrieve, transmit, or persist customer data, authentication secrets, personal data, or undisclosed incident details. Do not send messages or access any communications account.

## Provenance

Adapted from Anthropic's `internal-comms` at upstream commit `34040c9c568585f6929bedeaad110ad08f079624`, under Apache-2.0. The adaptation replaces company-specific example files with a fact-bound, Hermes-native drafting procedure.

## Rollback

Discard the draft or restore a version-controlled source document. Removing this skill from the profile-default skill directory stops future loading; it cannot retract text already shared by a user.
