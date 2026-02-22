# TODO: 1 - Import the AugmentedPromptAgent class
import os
from dotenv import load_dotenv
from workflow_agents.base_agents import AugmentedPromptAgent

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
base_url = os.getenv("BASE_URL")
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

print("Testing AugmentedPromptAgent...")
print("Prompt:", prompt)
print("Persona:", persona)

# TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
agent = AugmentedPromptAgent(
    base_url=base_url, 
    openai_api_key=openai_api_key, 
    persona=persona)

# TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
augmented_agent_response = agent.respond(prompt).strip()

# Print the agent's response
print("Response: ", augmented_agent_response)

# TODO: 4 - Add a comment explaining:
# - What knowledge the agent likely used to answer the prompt.
# - How the system prompt specifying the persona affected the agent's response.

print("The AugmentedPromptAgent used its built-in knowledge of world capitals to generate the response, and the specified persona influenced the tone and style of the answer.")