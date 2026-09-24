---
name: canvas-design
description: Plan an original single-page visual design artifact.
version: 0.1.0
author: Anthropic (upstream), Robert (gjlp25), Hermes Agent
license: Apache-2.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [canvas, visual, poster, design]
    related_skills: []
---

# Canvas Design Skill

Plan and create an original, single-page visual design artifact from a user brief, keeping the design visual-first and text sparse. This adaptation supplies no fonts, scripts, packages, or network behavior.

## When to Use

- A user explicitly requests an original poster, art print, cover, or other single-page visual design artifact.
- A user wants a design philosophy followed by a visual artifact.
- Do not use for restyling an existing artifact, copying a living artist's style, multi-page documents, logos, or production UI design.

## Prerequisites

- Confirm the requested output format and workspace destination.
- Keep the work original: use design attributes, not a named artist's protected style.
- Use only system-font fallbacks such as `Arial, sans-serif`, `Georgia, serif`, or `Courier New, monospace`; do not download or bundle fonts.

## Procedure

1. Write a concise design philosophy in a Markdown file: name, intent, space/form, color/material, scale/rhythm, and hierarchy. Completion: it is four to six distinct paragraphs and contains no copied artist style.
2. Extract a subtle conceptual reference from the user's brief without adding undisclosed facts. Completion: the reference guides composition rather than requiring explanatory text.
3. Define a single-page composition with a limited palette, visual hierarchy, margins, and sparse essential text. Completion: every element has a position, visual role, and breathing room.
4. Create the requested artifact only with tools already available in the active environment and only inside the approved workspace. Completion: the output is one page and no element is clipped or overlaps unintentionally.
5. Inspect the completed artifact with the appropriate available tool, such as `vision_analyze` for an image, and refine spacing, contrast, and legibility. Completion: the final composition remains visual-first and all content fits the canvas.

## Pitfalls

- Do not promise museum-quality output without an actual visual verification pass.
- Do not add a package, executable helper, binary font, or external resource merely to improve typography.
- Do not turn the design philosophy into a long text-heavy document.

## Security and Privacy

Use only user-provided material and the approved workspace. Do not retrieve external images or fonts, access authentication secrets, call external services, or write outside the task workspace.

## Provenance

Adapted from Anthropic's `canvas-design` at upstream commit `34040c9c568585f6929bedeaad110ad08f079624`, under Apache-2.0. The upstream font bundle and instructions to download fonts are intentionally omitted; no SIL OFL font asset is included.

## Rollback

Remove the generated design files from the workspace or restore a prior version with version control. Removing this skill from the profile-default skill directory disables future loading and leaves existing artifacts unchanged.
