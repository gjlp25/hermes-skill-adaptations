# Hermes adaptations of approved Anthropic skills

This repository contains exactly three text-only Hermes skill adaptations:

- `skills/theme-factory`: apply a named theme to an existing artifact.
- `skills/internal-comms`: draft a fact-bound internal communication.
- `skills/canvas-design`: plan an original one-page visual design artifact.

## License and provenance

The skills are adapted from `anthropics/skills` commit
`34040c9c568585f6929bedeaad110ad08f079624` under Apache-2.0. See `LICENSE`
and `NOTICE`. This bundle intentionally contains no upstream scripts, PDFs,
images, font binaries, package instructions, network behavior, or credentials.
No SIL OFL asset is included, so a font-license inventory is not needed.

## Profile-default installation staging

Stage, rather than install, the bundle by copying the three directories to a
temporary directory under a profile-default skills location. Inspect the staged
contents and activate only through the profile's approved skill installation
process. Do not replace or modify a live profile from this repository.

A safe staging shape is:

    <temporary-directory>/skills/theme-factory/SKILL.md
    <temporary-directory>/skills/internal-comms/SKILL.md
    <temporary-directory>/skills/canvas-design/SKILL.md

Activation is profile-default only; no project, customer, or shared profile is
targeted. To roll back, remove the three staged or installed skill directories.
Existing artifacts and drafts are not changed by removing a skill.

## Verification

Run the deterministic static contract tests without installing dependencies:

    python3 -m unittest tests/test_adapted_skills.py -v

The test suite checks the approved set, frontmatter, provenance, safety markers,
text-only asset policy, and staging documentation.
