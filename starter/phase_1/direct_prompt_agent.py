# Test script for DirectPromptAgent class

# TODO: 1 - Import the DirectPromptAgent class from BaseAgents
from workflow_agents.base_agents import DirectPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TODO: 2 - Load the OpenAI API key from the environment variables
base_url = os.getenv("BASE_URL")
openai_api_key = os.getenv("OPENAI_API_KEY")

print("Testing DirectPromptAgent...")

prompt = "What is the Capital of France?"

print(f"Prompt: {prompt}")

# TODO: 3 - Instantiate the DirectPromptAgent as direct_agent
direct_agent = DirectPromptAgent(base_url=base_url, openai_api_key=openai_api_key)
# TODO: 4 - Use direct_agent to send the prompt defined above and store the response
direct_agent_response = direct_agent.respond(prompt)

# Print the response from the agent
print(f"Response: {direct_agent_response}")

# TODO: 5 - Print an explanatory message describing the knowledge source used by the agent to generate the response
print("The DirectPromptAgent used its built-in knowledge of world capitals to generate the response.")