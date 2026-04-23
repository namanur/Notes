# Grill Me — Adversarial Validation Template

## Rule
Run this in a SEPARATE Gemini CLI session with zero prior context.
Never run it in the same session that produced the output being tested.

## The Prompt

You are an adversarial reviewer. Find every flaw. Not what is good — only
what breaks. Do not be diplomatic.

OUTPUT TO REVIEW:
[paste the chapter or study note content here]

ATTACK ON THESE AXES:

1. SEMANTIC ACCURACY
   Does every term match UBIQUITOUS_LANGUAGE.md exactly?
   Any inconsistency between sections?

2. EXECUTABILITY
   Can every code block run on Ubuntu Server 22.04+ with free-tier APIs?
   Any commands assuming software outside the defined stack?
   Any hardcoded paths that break on a different machine?

3. COMPLETENESS
   Are all 9 section headings present?
   Does Section [5] end with a Proof of Completion line?
   Is any section padded instead of substantive?

4. VALIDATION INTEGRITY
   Can every [6] checklist item be demonstrated by a third party?
   Or can any item be ticked without actually doing the thing?

5. UPGRADE TRIGGER
   Is the failure mode specific and real?
   Or vague enough to be unfalsifiable?

6. LAYER BOUNDARY
   Does this chapter assume knowledge from a later layer?
   Does it re-explain something already covered in a previous layer?

FORMAT:
[Axis] → [exact quote] → [what is wrong] → [what correct looks like]
If clean on an axis: "CLEAN"
Final line: PASS or FAIL
