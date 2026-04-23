# Gemini CLI Agent Logging Skill - agent-log

## Purpose
This skill provides automation for Gemini CLI agents to log their activities into the central `00_daily_logs/AGENT_ACTIVITY.md` file, following the established `agent_activity` procedure.

## Installation (Manual Step for User)
1.  Save this content as `agent-log.md` (or similar) in your `.gemini/skills/` directory.
2.  Run `/skills reload` in your Gemini CLI session to activate the skill.

## How to Use (for Gemini CLI Agent)
When a Gemini CLI agent completes a task or needs to log its activity, it should execute this skill. The skill will prompt the agent for the necessary information to construct the log entry.

## Skill Logic (for Gemini CLI Internal Use)
This section outlines the internal logic for the Gemini CLI agent to generate the log entry. This is a template for the *agent itself* to follow, or for a more advanced skill to automate.

### Input Prompts:
The agent should be prompted or should internally generate the following:

-   **Agent Name**: Automatically `Gemini CLI Agent`.
-   **Date**: Current date in `YYYY-MM-DD` format.
-   **Time**: Current time in `HH:MM` format.
-   **Goal**: What was the primary objective of this session? (e.g., "Implement YAML understanding notes.")
-   **Changes Made**: A bulleted list of specific changes.
    -   Example: `Created 10_Knowledge/Understanding YAML.md.`
    -   Example: `Modified 99_System/Topics.md.`
-   **Next Steps/Recommendations**: A bulleted list of follow-up actions.
    -   Example: `User to verify new YAML notes.`
    -   Example: `Consider updating all agents with the new logging procedure.`

### Log Entry Construction:
The Gemini CLI agent should assemble the input into the following Markdown format:

```markdown
### [[YYYY-MM-DD]] - [Agent Name] - [HH:MM]

**Goal:** [User provided Goal]

**Changes Made:**
[User provided Changes Made (bullet points)]

**Next Steps/Recommendations:**
[User provided Next Steps/Recommendations (bullet points)]

---
```

### Append to Log File:
The constructed log entry must then be appended to the end of `00_daily_logs/AGENT_ACTIVITY.md`.

**Example of an automated command (conceptual, depending on Gemini CLI's capabilities):**
```bash
gemini_cli --execute-skill agent-log --goal "Added new feature X" --changes "- created file Y - modified file Z" --next-steps "Review Y and Z"
```
Or, if the skill is more interactive, it would prompt for each piece of information.

---

**Note to User:** The actual implementation of this skill within the Gemini CLI environment depends on its skill-writing capabilities. This document provides the *blueprint* for what the skill should achieve. You might need to write a small script or configuration file that leverages Gemini CLI's features to execute this logic.
