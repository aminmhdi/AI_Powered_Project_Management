# AI-Powered Agentic Workflow for Project Management

A two-phase project that builds a reusable agent library (Phase 1) and composes those agents into an agentic workflow for product development (Phase 2). Follow the quickstart to run the provided agents and the sample workflow for the "Email Router" product spec.

## Quickstart

1. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

   See [requirements.txt](requirements.txt).

2. Create a `.env` in the repo root with your OpenAI key:

   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

   See [.env](.env).

3. Run Phase 1 agent tests (examples):
   - Direct prompt agent:
     ```sh
     python starter/phase_1/direct_prompt_agent.py
     ```
     Uses [`workflow_agents.base_agents.DirectPromptAgent`](starter/phase_1/workflow_agents/base_agents.py).
   - Augmented prompt agent:
     ```sh
     python starter/phase_1/augmented_prompt_agent.py
     ```
     Uses [`workflow_agents.base_agents.AugmentedPromptAgent`](starter/phase_1/workflow_agents/base_agents.py).
   - Knowledge-augmented agent:
     ```sh
     python starter/phase_1/knowledge_augmented_prompt_agent.py
     ```
     Uses [`workflow_agents.base_agents.KnowledgeAugmentedPromptAgent`](starter/phase_1/workflow_agents/base_agents.py).
   - RAG agent:
     ```sh
     python starter/phase_1/rag_knowledge_prompt_agent.py
     ```
     Uses [`workflow_agents.base_agents.RAGKnowledgePromptAgent`](starter/phase_1/workflow_agents/base_agents.py).
   - Evaluation, Routing, Action Planning:
     ```sh
     python starter/phase_1/evaluation_agent.py
     python starter/phase_1/routing_agent.py
     python starter/phase_1/action_planning_agent.py
     ```
     Use [`workflow_agents.base_agents.EvaluationAgent`](starter/phase_1/workflow_agents/base_agents.py), [`workflow_agents.base_agents.RoutingAgent`](starter/phase_1/workflow_agents/base_agents.py), and [`workflow_agents.base_agents.ActionPlanningAgent`](starter/phase_1/workflow_agents/base_agents.py).

4. Run Phase 2 agentic workflow:
   ```sh
   python starter/phase_2/agentic_workflow.py
   ```
   Uses the Product Spec at [starter/phase_2/Product-Spec-Email-Router.txt](starter/phase_2/Product-Spec-Email-Router.txt) and agent implementations in [starter/phase_2/workflow_agents/base_agents.py](starter/phase_2/workflow_agents/base_agents.py). Workflow output/log example: [output/phase_2/logs.txt](output/phase_2/logs.txt).

## Project Structure (key files)

- Overview: [project_overview.md](project_overview.md)
- Phase 1 starter:
  - Readme: [starter/phase_1/readme.md](starter/phase_1/readme.md)
  - Agents implementation: [starter/phase_1/workflow_agents/base_agents.py](starter/phase_1/workflow_agents/base_agents.py)
  - Test scripts:
    - [starter/phase_1/direct_prompt_agent.py](starter/phase_1/direct_prompt_agent.py)
    - [starter/phase_1/augmented_prompt_agent.py](starter/phase_1/augmented_prompt_agent.py)
    - [starter/phase_1/knowledge_augmented_prompt_agent.py](starter/phase_1/knowledge_augmented_prompt_agent.py)
    - [starter/phase_1/rag_knowledge_prompt_agent.py](starter/phase_1/rag_knowledge_prompt_agent.py)
    - [starter/phase_1/evaluation_agent.py](starter/phase_1/evaluation_agent.py)
    - [starter/phase_1/routing_agent.py](starter/phase_1/routing_agent.py)
    - [starter/phase_1/action_planning_agent.py](starter/phase_1/action_planning_agent.py)
- Phase 2 starter:
  - Workflow orchestrator: [starter/phase_2/agentic_workflow.py](starter/phase_2/agentic_workflow.py)
  - Agents (phase 2 copy): [starter/phase_2/workflow_agents/base_agents.py](starter/phase_2/workflow_agents/base_agents.py)
  - Product spec: [starter/phase_2/Product-Spec-Email-Router.txt](starter/phase_2/Product-Spec-Email-Router.txt)
- Outputs: [output/phase_2/logs.txt](output/phase_2/logs.txt)

## Agents (implemented classes)

- [`workflow_agents.base_agents.DirectPromptAgent`](starter/phase_1/workflow_agents/base_agents.py)
- [`workflow_agents.base_agents.AugmentedPromptAgent`](starter/phase_1/workflow_agents/base_agents.py)
- [`workflow_agents.base_agents.KnowledgeAugmentedPromptAgent`](starter/phase_1/workflow_agents/base_agents.py)
- [`workflow_agents.base_agents.RAGKnowledgePromptAgent`](starter/phase_1/workflow_agents/base_agents.py)
- [`workflow_agents.base_agents.EvaluationAgent`](starter/phase_1/workflow_agents/base_agents.py)
- [`workflow_agents.base_agents.RoutingAgent`](starter/phase_1/workflow_agents/base_agents.py)
- [`workflow_agents.base_agents.ActionPlanningAgent`](starter/phase_1/workflow_agents/base_agents.py)

## How it works (brief)

- Phase 1 builds and tests isolated agent classes that wrap OpenAI calls and simple orchestration logic.
- Phase 2 composes those agents: an Action Planning agent extracts steps from a high-level prompt, a Routing agent selects the appropriate specialist agent for each step, specialist Knowledge-Augmented agents generate outputs, and Evaluation agents iteratively validate/refine results. See [starter/phase_2/agentic_workflow.py](starter/phase_2/agentic_workflow.py).

## Notes & troubleshooting

- Ensure your OpenAI API key is set and valid in `.env`.
- Model names and embeddings are configured in the agent code (search for `gpt-3.5-turbo` and `text-embedding-3-large` in the agent files).
- If you need to see an example run, inspect [output/phase_2/logs.txt](output/phase_2/logs.txt).

## References

- Starter instructions: [starter/phase_1/readme.md](starter/phase_1/readme.md), [starter/phase_2/readme.md](starter/phase_2/readme.md)
- Product spec used by Phase 2: [starter/phase_2/Product-Spec-Email-Router.txt](starter/phase_2/Product-Spec-Email-Router.txt)
