# Stitch-to-Compose Skill
Translates Google Stitch `DESIGN.md` design specs into Android UI code.

## Instructions
1. When you have a `DESIGN.md` from Google Stitch, provide it to this skill.
2. The skill identifies design tokens (colors, fonts, spacing) and translates them to Android `Theme.kt` (Compose) or `colors.xml` (XML).
3. It creates an overlay screen with a "Blocked" state that matches your Stitch design.

## Available Resources
- `assets/template_overlay.xml`: Standard "Blocked" UI structure.
