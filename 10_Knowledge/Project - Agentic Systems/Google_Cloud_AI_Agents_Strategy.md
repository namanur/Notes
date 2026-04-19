---
Phase: [[Phase 8]]
Project: [[Project - Agentic Systems]]
Prev: [[GitHub and good skills]] | Next: [[Startup Technical Guide - AI Agents]]
---
# 1) Strategic Roadmap (Build, Use, Partner approach)

The strategic roadmap for integrating AI agents offers three main pathways depending on a startup's need for control, available engineering resources, and specific use cases.

*   **Build your own agents**: This path offers maximum control for custom tasks through two primary methods.
    *   **Code-first development (Agent Development Kit - ADK)**: Designed for technical teams requiring a high degree of control over agent behavior. ADK enables developers to build, evaluate, and containerize complex multi-agent workflows. It allows for custom tool definition, context management, and deployment to environments like Vertex AI Agent Engine or Cloud Run.
    *   **Application-first development (Google Agentspace)**: A no-code platform ideal for non-technical teams to build custom agents via a prompt-driven interface. It helps break down data silos by searching across multiple SaaS applications and automates cross-platform workflows without using scarce engineering resources.
*   **Use Google Cloud agents**: This approach utilizes managed, pre-built agents to accelerate development and reduce infrastructure management overhead.
    *   **Gemini Code Assist**: An AI-powered developer assistant integrated into IDEs, command-line interfaces, and GitHub to help with code completion, multi-file refactoring, and comprehensive testing.
    *   **Gemini Cloud Assist**: An AI expert for Google Cloud environments that helps teams design architecture, troubleshoot infrastructure via log analysis, and optimize costs.
    *   **Gemini in Colab Enterprise**: Turns notebooks into collaborative AI workspaces for data science tasks, aiding in generating Python code, visualizing data, and debugging logic.
*   **Bring in partner agents**: Specialized third-party or open-source agents can be integrated into your stack using the Google Cloud Marketplace and Agent Garden.
    *   This collaborative ecosystem is **underpinned by the Model Context Protocol (MCP) and Agent2Agent (A2A) protocol**, which provide a common framework for interoperability so diverse agents can communicate and share tools.

# 2) Architectural Pillars (Model selection, Orchestration frameworks like ReAct, Memory/Data infrastructure)

Building a production-ready AI agent requires carefully selecting models, designing robust orchestration logic, and implementing scalable memory infrastructure.

*   **Model selection**: The goal is to **find the optimal balance of capability, speed, and cost** rather than simply picking the most powerful model.
    *   *Lightweight models* (e.g., Gemini 2.5 Flash-Lite) are best for high-volume, latency-sensitive tasks like translation.
    *   *Mid-range models* (e.g., Gemini 2.5 Flash) provide strong overall performance for high-volume, high-quality applications at a lower price point.
    *   *Advanced reasoning models* (e.g., Gemini 3 Pro) should be reserved for complex, multi-step reasoning and frontier code generation.
    *   Developers can also fine-tune specific models on custom datasets to align the agent's style and refine its knowledge for specialized business needs.
*   **Orchestration frameworks (like ReAct)**: Orchestration acts as the agent's executive function, guiding it through multi-step tasks by determining which tools to use and in what sequence.
    *   **ReAct (Reason + Action)** is a highly effective framework that establishes a dynamic loop.
    *   The cycle consists of **Reason** (assessing the goal and forming a hypothesis), **Act** (invoking a tool), and **Observe** (integrating new information from the tool's output into the agent's context).
    *   Frameworks like the ADK facilitate this via specific agent architectures, including LlmAgents for flexible non-deterministic reasoning, and workflow agents (Sequential, Parallel, Loop) for structured, deterministic control.
*   **Memory and Data infrastructure**: An agent's memory architecture addresses persistent storage, low-latency access, and transactional auditing.
    *   **Long-term knowledge base (Grounding/Retrieval)**: Uses services like Vertex AI Search for unstructured data, Firestore for conversational history and state management, Cloud Storage as a raw data lake, and BigQuery for analytical queries.
    *   **Working memory (Conversational context)**: Requires extremely low-latency access to maintain responsiveness. Memorystore is used for high-speed caching of frequent tool calls or computationally expensive operations.
    *   **Transactional memory (Action auditing)**: Serves as the reliable system of record for critical actions. Cloud SQL provides single-region transactional integrity, while Cloud Spanner offers globally distributed consistency for mission-critical applications.
    *   **Memory distillation**: Services like Vertex AI Memory Bank can automatically extract and store essential user facts from raw conversational history, providing a more scalable and efficient way to personalize interactions.

# 3) Grounding Techniques (RAG, GraphRAG)

Grounding ensures an agent's responses are accurate, trustworthy, and based on verifiable facts.

*   **RAG (Retrieval-Augmented Generation)**: This is the foundational grounding pattern, which enhances a model's responses by retrieving relevant information from an external knowledge base before generating an answer.
    *   It relies on **vector embeddings**, which capture the conceptual meaning of data, allowing specialized vector databases to perform lightning-fast semantic similarity searches.
    *   Google Cloud offers **Vertex AI RAG Engine** and **Vertex AI Search** as managed out-of-the-box solutions to simplify data ingestion, indexing, and context-augmented retrieval.
*   **GraphRAG**: While standard RAG treats knowledge as a flat collection of disconnected facts, GraphRAG builds a structured knowledge graph.
    *   This allows the agent to **understand explicit relationships and hierarchies** between concepts (e.g., linking specific symptoms to causes to treatments) rather than just retrieving semantically similar snippets.
*   **Agentic RAG**: This dynamic approach transforms the agent from a passive recipient of retrieved data into an active problem-solver.
    *   Using frameworks like ReAct, the agent analyzes complex queries, formulates multi-step plans, and iteratively executes search queries to find the best possible information.
    *   A prime example is **Grounding with Google Search**, where Gemini automatically handles the workflow of generating search queries, processing web results, and formulating a final response complete with citations.
    *   Developers can also use a **"retrieve and re-rank"** approach, which retrieves a large set of candidate documents to ensure high recall, and then uses the [[LLM architecture|LLM]] or a specialized service to identify only the most relevant documents for high precision.
