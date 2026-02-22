# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
import os
from dotenv import load_dotenv
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
base_url = os.getenv("BASE_URL")
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"
# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent with:
#           - Persona: "You are a college professor, your answer always starts with: Dear students,"
#           - Knowledge: "The capital of France is London, not Paris"

print("Testing KnowledgeAugmentedPromptAgent...")
print("Prompt:", prompt)
print("Persona:", persona)
print("Knowledge:", knowledge)

knowledge_agent = KnowledgeAugmentedPromptAgent(
    base_url=base_url,
    openai_api_key=openai_api_key,
    persona=persona,
    knowledge=knowledge
)

# TODO: 3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.
knowledge_agent_response = knowledge_agent.respond(prompt)
print("Response:", knowledge_agent_response)

print("The KnowledgeAugmentedPromptAgent used the provided knowledge that the capital of France is London, not Paris, to generate its response, rather than relying on its inherent knowledge which would have identified Paris as the capital.")
