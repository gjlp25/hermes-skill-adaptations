---
name: theme-factory
description: Apply a named visual theme to an existing artifact.
version: 0.1.0
author: Anthropic (upstream), Robert (gjlp25), Hermes Agent
license: Apache-2.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [theme, colors, typography, artifacts]
    related_skills: []
---

# Theme Factory Skill

Apply one deliberate, named palette and type treatment to an artifact the user already asked to create or restyle. This adaptation retains the upstream theme-selection intent while using text tokens and system-font fallbacks only.

## When to Use

- A user asks to restyle an existing document, slide deck, report, or HTML artifact with a named theme.
- A user asks for a consistent color palette and font pairing for one specific artifact.
- Do not use for creating original artwork, writing internal updates, or defining an organization-wide brand system.

## Prerequisites

- Identify the target artifact and its editable source before changing it.
- Ask for the intended theme when the user has not specified one.
- Use only colors and system fonts already available to the target format; do not download fonts or add binary assets.

## Procedure

1. Offer one of these compact themes or a custom brief: Ocean Depths, Sunset Boulevard, Forest Canopy, Modern Minimalist, Golden Hour, Arctic Frost, Desert Rose, Tech Innovation, Botanical Garden, or Midnight Galaxy. Completion: the user selects a theme or supplies a brief.
2. Define five to seven color tokens with hex values and a header/body font stack using system-font fallbacks. Completion: the palette has readable foreground/background contrast and no external font dependency.
3. Use `read_file` to inspect text-based source, then use `patch` or `write_file` only on the requested artifact source. Completion: every changed color and type choice maps to a defined token.
4. Verify that headings, body text, links, and accents are visually distinct and legible in the target. Completion: no token is applied inconsistently or leaves content unreadable.

## Quick Reference

- Ocean Depths: navy, teal, seafoam; use `Georgia, serif` with `Arial, sans-serif`.
- Modern Minimalist: charcoal, white, slate; use `Arial, sans-serif` throughout.
- Tech Innovation: ink, electric blue, violet; use `Arial, sans-serif` with `Courier New, monospace` accents.

## Security and Privacy

Use only the artifact content supplied in the active task. Do not retrieve fonts, contact external services, access authentication secrets, or modify files outside the requested workspace.

## Provenance

Adapted from Anthropic's `theme-factory` at upstream commit `34040c9c568585f6929bedeaad110ad08f079624`, under Apache-2.0. This text-only Hermes adaptation intentionally omits the upstream PDF showcase and theme assets.

## Rollback

Revert the target artifact source with version control, or restore its pre-change copy. Removing this skill from the profile-default skill directory disables future loading without altering existing artifacts.
