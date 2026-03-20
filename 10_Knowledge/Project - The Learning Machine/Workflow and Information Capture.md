# Workflow and Information Capture

The goal of this workflow is to capture information from external sources (YouTube, Research, LLMs) and process it into the Knowledge layer (Memory) through the Daily Logs (Runtime).

## 1. Daily Logs (Runtime Execution)
The `00_daily_logs/` folder is where the day-to-day action happens. 
- **Purpose**: To track what was done, what was learned, and what is next.
- **Workflow**: 
    1.  Create a daily log using the `Daily log template.md`.
    2.  Use it as a scratchpad throughout the day.
    3.  Review it at the end of the day to extract permanent notes for the `10_Knowledge/` layer.

## 2. Research Workflow
Research is the process of finding and validating information.
- **Inquiry**: Start with a question or a problem.
- **Investigation**: Use LLMs, official docs, or YouTube lectures.
- **Validation**: Verify the information (run the code, cross-reference sources).
- **Consolidation**: Write the findings in your own words.

## 3. Information Capture
Capture information where it happens, but don't let it clutter the vault.
- **Fleeting Notes**: Use the Daily Log for quick captures.
- **Literature Notes**: Create temporary notes for specific lectures or articles.
- **LLM Assistance**: Use LLMs to summarize or explain complex topics, then rewrite them to ensure personal understanding.

## 4. Knowledge Indexing
Indexing ensures that information can be found when needed.
- **MOCs (Map of Content)**: Use `99_System/Topics.md` as the high-level index for the learning curve.
- **Internal Links**: Every note should be linked to at least one other note to maintain a connected web.
- **Folder Structure**: 
    - `00_daily_logs/`: Recent, messy thinking.
    - `10_Knowledge/`: Clean, organized permanent notes.
    - `99_System/`: Meta-notes about how the system works.

## 5. The Feedback Loop
The most effective learning loop:
1.  **Capture**: Record the raw idea.
2.  **Process**: Filter and summarize.
3.  **Synthesize**: Connect it to what you already know (Linking).
4.  **Recall**: Use the notes as a reference when building or learning new things.

---
*Related Topics:* [[Personal Knowledge Management]], [[Git and GitHub Setup]]