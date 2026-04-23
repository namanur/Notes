# Chapter 05: Domain-Driven Design For Agents
> Layer: L1 | Prerequisite: L0_C04
> Context injected from: UBIQUITOUS_LANGUAGE.md

## [1] Concept Explanation
Domain-Driven Design (DDD) for agents is the practice of constraining an agent's **Reasoning** and **Action** within a strictly defined linguistic and functional boundary. Unlike general software DDD, which focuses on code structure, Agentic DDD focuses on **Semantic Grounding**. 

The mechanics involve three core pillars:
- **Maintenance**: Treating your `UBIQUITOUS_LANGUAGE.md` as a living contract. Every time a new **Tool** is added to the **Harness**, its name and purpose must be reconciled with this file.
- **Reference**: The agent must ingest the domain language in every turn to ensure that **Perception** (interpreting user intent) matches the **Action** (tool execution). If the user says "reconcile," the agent must know if that means a database sync or an accounting verification.
- **Drift Detection**: Identifying when an agent begins to use "hallucinated terminology"—terms that sound plausible but are not defined in the domain. This is often the first sign of reasoning decoupling.

## [2] Why This Layer Exists
Layer 1 (Discipline) exists to prevent the "Black Box" failure of Layer 0 prototypes. In L0, you build a **Harness** that works. In L1, you ensure it works *predictably*. Without DDD, an agent is a tourist in your codebase—it knows the words but doesn't understand the local laws. By scoping the semantic domain, you reduce the **Context Window** noise and prevent "feature creep" where a simple file-organizer agent suddenly decides it's a project manager.

## [3] Stack Integration
- **Gemini CLI**: Acts as the primary interface. Use the `--context` flag or include `UBIQUITOUS_LANGUAGE.md` in the system prompt to ground the model.
- **OpenRouter Fallback**: When switching models (e.g., Gemini to Claude), the DDD contract ensures behavioral consistency despite differing model weights.
- **Dell Ubuntu Server**: Stores the **Memory** (SQLite). Your database schema should mirror the ubiquitous language. A table named `ledgers` is better than `data_store_01`.
- **ASUS VivoBook**: The development environment where you perform "Drift Audits" using shell tools.

## [4] What To Read / Watch / Study
- **Reading**: *Domain-Driven Design* by Eric Evans (Focus on "Ubiquitous Language" and "Bounded Contexts").
- **Study Note**: `[[domain_driven_design]]` in the `STUDY_NOTES/` folder.
- **Video**: Search for "Small Language Models and Domain Specificity" to understand why smaller, grounded contexts often outperform massive, ungrounded ones.
- **Accounting Parallel**: Review GST/VAT classification rules; they are the ultimate real-world implementation of a "Ubiquitous Language."

## [5] Hands-On Execution
### Exercise: Grounding the C04 Harness
1. **Create the Language File**: Navigate to your C04 harness directory and create `language.md`.
2. **Define the Terms**: Copy the core definitions from `UBIQUITOUS_LANGUAGE.md` that apply *only* to that harness.
3. **Inject as Context**: Modify your agent's execution script to read this file before taking any input.
4. **The Drift Test**: Ask the agent to perform an action using a term *not* in the file.
   - *Success*: The agent asks for clarification or maps it to a known term.
   - *Failure*: The agent hallucinates a new tool or process.

**Proof of Completion**: Run `grep` on your harness's `AGENT_MANIFEST.md` and verify that 100% of the tools used match the terms in your `language.md`.

## [6] Validation Criteria
- **Grep Audit**: `grep -f UBIQUITOUS_LANGUAGE.md SESSION_LOG.md` should return high-density matches.
- **Boundary Check**: No tool in the harness should perform an action that falls outside the defined "Semantic Domain."
- **Grill Me Proof**: Pass your `AGENT_MANIFEST.md` to a "Griller" agent and ask: "Which of these tools violate our ubiquitous language?"

## [7] Upgrade Trigger
You are ready for the next chapter when you encounter **Invisible Semantic Failures**. These are bugs where the code runs without errors, the agent claims success, but the result is "wrong" because the agent misinterpreted a domain-specific instruction (e.g., it "archived" by deleting because it didn't know your domain requires zipping). When you realize that logic errors are actually language errors, you have mastered the Discipline of DDD.

## [8] Session Log Entry
"Implemented DDD grounding for the B2B Service Agent. Discovered that the agent was confusing 'Client Onboarding' with 'User Registration.' Updated `UBIQUITOUS_LANGUAGE.md` to separate the two. Drift audit confirmed 95% compliance in the latest reasoning loop."

## [9] Connections
- **Previous**: `[[L0_C04_Your_First_Harness]]` - The chassis we are now disciplining.
- **Next**: `[[L1_C06_Test_Driven_Development_For_Agents]]` - How to turn these language definitions into executable tests.
- **Reference**: `[[UBIQUITOUS_LANGUAGE]]` - The master dictionary.
