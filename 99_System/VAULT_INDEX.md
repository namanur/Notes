# VAULT INDEX — Agent Architect Manual v2.2

## Learning
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L0_Foundation/L0_C01_What_Is_An_Agent.md|L0_C01_What_Is_An_Agent]] — Five components of an agent and the no-local-LLM rule | Layer: L0 | Session: 001 | Status: complete | Bytes: 3985
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L0_Foundation/L0_C02_Your_Stack_And_Environment.md|L0_C02_Your_Stack_And_Environment]] — Hardware roles (VivoBook vs Dell) and provider fallbacks | Layer: L0 | Session: 001 | Status: complete | Bytes: 4391
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L0_Foundation/L0_C03_Context_And_Memory_Basics.md|L0_C03_Context_And_Memory_Basics]] — Mechanical tokens vs structured SQLite memory | Layer: L0 | Session: 001 | Status: complete | Bytes: 4770
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L0_Foundation/L0_C04_Your_First_Harness.md|L0_C04_Your_First_Harness]] — Minimal execution chassis using JSON-RPC | Layer: L0 | Session: 001 | Status: complete | Bytes: 3597

## Generated Context
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/GENERATED_CONTEXT/L0_Foundation_context.md|L0_Foundation_context]] — Distilled concepts and terms from the foundation layer | Layer: L0 | Session: 001 | Status: complete | Bytes: 2266

## System
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/UBIQUITOUS_LANGUAGE.md|UBIQUITOUS_LANGUAGE]] — Binding terminology for the entire manual | Layer: System | Session: 001 | Status: complete | Bytes: 1701
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/_SYSTEM/FALLBACK_CHAIN.sh|FALLBACK_CHAIN.sh]] — Script for model failover during rate limits | Layer: System | Session: 001 | Status: complete | Bytes: 1050
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/_SYSTEM/GRILL_ME_TEMPLATE.md|GRILL_ME_TEMPLATE.md]] — Adversarial validation template for quality checks | Layer: System | Session: 001 | Status: complete | Bytes: 1441
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/_SYSTEM/AGENT_MANIFEST.md|AGENT_MANIFEST.md]] — Definitions of agent roles and workflows | Layer: System | Session: 001 | Status: complete | Bytes: 562
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/_SYSTEM/RESUME_INSTRUCTIONS.md|RESUME_INSTRUCTIONS.md]] — Procedures for resuming interrupted build sessions | Layer: System | Session: 001 | Status: complete | Bytes: 272
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/_SYSTEM/ORCHESTRATOR_PROMPT.md|ORCHESTRATOR_PROMPT.md]] — Core instructions for the build orchestrator | Layer: System | Session: 001 | Status: complete | Bytes: 30649
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/_SYSTEM/validate_disk_state.sh|validate_disk_state.sh]] — Integrity check script for the manual files | Layer: System | Session: 001 | Status: complete | Bytes: 1661

## Navigation
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/00_MANUAL_INDEX.md|00_MANUAL_INDEX]] — High-level Table of Contents and Build Status | Layer: System | Session: 001 | Status: complete | Bytes: 695
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/TOPIC_MAP.md|TOPIC_MAP]] — Mapping of established concepts to their chapters | Layer: System | Session: 001 | Status: complete | Bytes: 641

## Logs
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/_SYSTEM/SESSION_LOG.md|SESSION_LOG]] — The runtime ledger of the build lifecycle | Layer: System | Session: 001 | Status: complete | Bytes: 2997

## Layer 1: Discipline
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L1_Discipline/L1_C05_Domain_Driven_Design_For_Agents.md|L1_C05_Domain_Driven_Design_For_Agents]] — Semantic grounding and ubiquitous language maintenance | Layer: L1 | Session: 001 | Status: complete | Bytes: 4996
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L1_Discipline/L1_C06_MCP_Architecture_Proper.md|L1_C06_MCP_Architecture_Proper]] — Formalizing interaction boundaries with MCP and JSON-RPC | Layer: L1 | Session: 001 | Status: complete | Bytes: 3902
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L1_Discipline/L1_C07_TDD_And_Execution_Loops.md|L1_C07_TDD_And_Execution_Loops]] — Enforcing execution rigor through TDD and SQLite state tracking | Layer: L1 | Session: 001 | Status: complete | Bytes: 4457
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/GENERATED_CONTEXT/L1_Discipline_context.md|L1_Discipline_context]] — Distilled concepts and tools from the discipline layer | Layer: L1 | Session: 001 | Status: complete | Bytes: 3248

## Study Notes
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/STUDY_NOTES/domain_driven_design.md|STUDY_NOTES/domain_driven_design]] — Study note for Domain-Driven Design: confirmed before L1_C05, Grill Me passed: yes | Layer: L1 | Status: confirmed

## Layer 2: Production
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L2_Production/L2_C08_Cloud_APIs_And_No_Local_LLM_Rule.md|L2_C08_Cloud_APIs_And_No_Local_LLM_Rule]] — Architectural argument for cloud-only reasoning and fallback mechanisms | Layer: L2 | Session: 001 | Status: complete | Bytes: 5035
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L2_Production/L2_C09_AgentOps_Sandboxing_And_Permissions.md|L2_C09_AgentOps_Sandboxing_And_Permissions]] — Monitoring, tracing, and secures execution through firejail containment | Layer: L2 | Session: 001 | Status: complete | Bytes: 5147
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L2_Production/L2_C10_Deep_Modules_And_Thick_Boundaries.md|L2_C10_Deep_Modules_And_Thick_Boundaries]] — Managing complexity and preventing silent failures via strict defensive contracts | Layer: L2 | Session: 001 | Status: complete | Bytes: 4632
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/GENERATED_CONTEXT/L2_Production_context.md|L2_Production_context]] — Distilled concepts and tools from the production layer | Layer: L2 | Session: 001 | Status: complete | Bytes: 3325

## Layer 3: Scale
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L3_Scale/L3_C11_Multi_Agent_Swarms.md|L3_C11_Multi_Agent_Swarms]] — Decentralized coordination via the Blackboard pattern and specialist isolation | Layer: L3 | Session: 001 | Status: complete | Bytes: 4881
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L3_Scale/L3_C12_Governance_And_Agentspace.md|L3_C12_Governance_And_Agentspace]] — Safety boundaries, audit trails, and human-in-the-loop checkpoints | Layer: L3 | Session: 001 | Status: complete | Bytes: 4879
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/GENERATED_CONTEXT/L3_Scale_context.md|L3_Scale_context]] — Distilled concepts and tools from the scale layer | Layer: L3 | Session: 001 | Status: complete | Bytes: 3921

## Study Notes (Confirmed)
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/STUDY_NOTES/multi_agent_swarms.md|STUDY_NOTES/multi_agent_swarms]] — Study note for Multi-Agent Swarms: confirmed before L3_C11, Grill Me passed: yes | Layer: L3 | Status: confirmed

## Layer 4: Leverage
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L4_Leverage/L4_C13_Open_Source_Positioning.md|L4_C13_Open_Source_Positioning]] — Positioning builds as public professional signals through standardized MCP harnesses | Layer: L4 | Session: 001 | Status: complete | Bytes: 5336
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L4_Leverage/L4_C14_Micro_SaaS_And_MCP_Packaging.md|L4_C14_Micro_SaaS_And_MCP_Packaging]] — Packaging reasoning loops and outcomes as sellable B2B service assets | Layer: L4 | Session: 001 | Status: complete | Bytes: 4697
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/L4_Leverage/L4_C15_Certification_Pathways.md|L4_C15_Certification_Pathways]] — Mapping manual mastery to CCA-F, MCP, and Google Cloud professional benchmarks | Layer: L4 | Session: 001 | Status: complete | Bytes: 4761
- [[10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/GENERATED_CONTEXT/L4_Leverage_context.md|L4_Leverage_context]] — Distilled concepts and tools from the leverage layer | Layer: L4 | Session: 001 | Status: complete | Bytes: 3026
