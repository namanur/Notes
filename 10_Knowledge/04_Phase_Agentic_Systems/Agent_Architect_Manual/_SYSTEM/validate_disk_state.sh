#!/bin/bash
ROOT="/home/naman/Documents/Notes/10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual"

echo "=== DISK VALIDATION === $(date -u +%Y-%m-%dT%H:%M)"

FILES=(
  "_SYSTEM/SESSION_LOG.md"
  "_SYSTEM/FALLBACK_CHAIN.sh"
  "UBIQUITOUS_LANGUAGE.md"
  "L0_Foundation/L0_C01_What_Is_An_Agent.md"
  "L0_Foundation/L0_C02_Your_Stack_And_Environment.md"
  "L0_Foundation/L0_C03_Context_And_Memory_Basics.md"
  "L0_Foundation/L0_C04_Your_First_Harness.md"
  "GENERATED_CONTEXT/L0_Foundation_context.md"
  "L1_Discipline/L1_C05_Domain_Driven_Design_For_Agents.md"
  "L1_Discipline/L1_C06_MCP_Architecture_Proper.md"
  "L1_Discipline/L1_C07_TDD_And_Execution_Loops.md"
  "GENERATED_CONTEXT/L1_Discipline_context.md"
  "L2_Production/L2_C08_Cloud_APIs_And_No_Local_LLM_Rule.md"
  "L2_Production/L2_C09_AgentOps_Sandboxing_And_Permissions.md"
  "L2_Production/L2_C10_Deep_Modules_And_Thick_Boundaries.md"
  "GENERATED_CONTEXT/L2_Production_context.md"
  "L3_Scale/L3_C11_Multi_Agent_Swarms.md"
  "L3_Scale/L3_C12_Governance_And_Agentspace.md"
  "GENERATED_CONTEXT/L3_Scale_context.md"
  "L4_Leverage/L4_C13_Open_Source_Positioning.md"
  "L4_Leverage/L4_C14_Micro_SaaS_And_MCP_Packaging.md"
  "L4_Leverage/L4_C15_Certification_Pathways.md"
  "GENERATED_CONTEXT/L4_Leverage_context.md"
  "TOPIC_MAP.md"
  "00_MANUAL_INDEX.md"
)

MISSING=0
for F in "${FILES[@]}"; do
  FP="$ROOT/$F"
  if [ -s "$FP" ]; then
    echo "[OK]      $F ($(wc -c < "$FP") bytes)"
  else
    echo "[MISSING] $F"
    MISSING=$((MISSING+1))
  fi
done

echo ""
echo "Result: $MISSING file(s) missing or empty"
echo "Any file missing but marked [x] in SESSION_LOG = ghost entry — clear it"
