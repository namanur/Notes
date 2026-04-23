# Wiki Maintainer Skill
**Purpose:** Orchestrate the Karpathy "LLM Wiki" pattern, compiling active knowledge from notes into a persistent, interlinked library.

## When to use
- At the end of a learning sub-phase (e.g., finishing a "Chapter" in `SYLLABUS.md`).
- When a new source is added to `Documents/llm-wiki/raw/`.
- When the user asks to "compile insights" or "sync to wiki."

## Instructions
1. **Identify Source**: Select content from `00_daily_logs/` or `10_Knowledge/` that represents completed, high-signal knowledge.
2. **Entity Check**: Check `Documents/llm-wiki/index.md` to see if an entity/concept page already exists.
3. **Draft/Update Page**: 
    - Create/Update pages in `Documents/llm-wiki/` following the YAML metadata standards in `WIKI_SCHEMA.md`.
    - Use `Double Bracket` syntax for all cross-references to ensure Obsidian compatibility.
4. **Update Navigation**: 
    - Append a summary entry to `Documents/llm-wiki/index.md`.
    - Record the operation type (Compile/Update) in `Documents/llm-wiki/log.md`.
5. **Verify Links**: Run a quick scan to ensure the new/updated page is reachable from the index.

## Resources
- Schema: `Documents/llm-wiki/WIKI_SCHEMA.md`
- Index: `Documents/llm-wiki/index.md`
- Log: `Documents/llm-wiki/log.md`
