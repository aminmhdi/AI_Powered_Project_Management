# agentic_workflow.py

"""
Implement support functions for routed tasks.

Reviewer Note

Spec: Implement support functions for routed tasks.

the specification doesn't pass.

The three support functions are defined and they do accept a query, call the corresponding KnowledgeAugmentedPromptAgent.respond(), and pass that output to the corresponding EvaluationAgent.evaluate().
The functions do not correctly return the final validated response: they return the raw response from the knowledge agent instead of the evaluation output (for example, final_response).
The functions check evaluation["result"] and evaluation["feedback"], but EvaluationAgent.evaluate() returns final_response, final_evaluation, and iterations, so this mismatch can break execution and prevents correct validated return behavior.
What to fix:

Update each support function in starter/phase_2/agentic_workflow.py to return evaluation["final_response"] (or equivalent validated field) instead of returning the raw knowledge-agent response.
Replace the result/feedback key checks with logic that uses the actual evaluation keys (for example final_evaluation and final_response) so the functions work with the current EvaluationAgent output format.
Support functions (e.g., product_manager_support_function, program_manager_support_function, development_engineer_support_function) are defined.Each support function:

Accepts an input query (a step from the action plan).
Calls the respond() method of its corresponding KnowledgeAugmentedPromptAgent.
Passes the response from the Knowledge Agent to the evaluate() method of its corresponding EvaluationAgent.
Returns the final, validated response (e.g., from the 'final_response' key of the evaluation result). 
"""

"""
Produce a final, structured output for the Email Router project.

Reviewer Note

Spec: Produce a final, structured output for the Email Router project.

the specification doesn't pass.

The script does produce a final output, but the final output is only a generic documentation-task list (the last step), not a comprehensive project plan containing user stories, product features, and detailed engineering tasks together.
User stories in the run log do follow the expected “As a [user], I want [action] so that [benefit]” style, so that part is present.
The required product feature structure (Feature Name, Description, Key Functionality, User Benefit) is not present in the produced output.
The required engineering task structure (Task ID, Task Title, Related User Story, Description, Acceptance Criteria, Estimated Effort, Dependencies) is also not present in the produced output.
What to fix:

Update the workflow so the generated final output consolidates all required sections: user stories, structured product features, and structured engineering tasks.
Ensure the Program Manager and Development Engineer outputs are enforced in the exact required field formats, and print that consolidated structured plan as the final workflow result.
The agentic_workflow.py script, when run with the Product-Spec-Email-Router.txt and a suitable high-level prompt (e.g., workflow_prompt from starter code, or similar, focusing on generating a full project plan), produces a final output.
This output represents a comprehensively planned project for the Email Router, including user stories, product features, and detailed engineering tasks.
The generated user stories follow the structure: "As a [type of user], I want [an action or feature] so that [benefit/value]."
The generated product features follow the structure: "Feature Name:...", "Description:...", "Key Functionality:...", "User Benefit:..."
The generated engineering tasks follow the structure: "Task ID:...", "Task Title:...", "Related User Story:...", "Description:...", "Acceptance Criteria:...", "Estimated Effort:...", "Dependencies:..."
"""

# TODO: 1 - Import the following agents: ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent from the workflow_agents.base_agents module
import workflow_agents.base_agents as base_agents

import os
from dotenv import load_dotenv

# TODO: 2 - Load the OpenAI key into a variable called openai_api_key
load_dotenv()
base_url = os.getenv("BASE_URL")
openai_api_key = os.getenv("OPENAI_API_KEY")

# load the product spec
# TODO: 3 - Load the product spec document Product-Spec-Email-Router.txt into a variable called product_spec
with open("starter/phase_2/Product-Spec-Email-Router.txt", "r") as f:
    product_spec = f.read()

# Instantiate all the agents
    
# Action Planning Agent
knowledge_action_planning = (
    "Stories are defined from a product spec by identifying a "
    "persona, an action, and a desired outcome for each story. "
    "Each story represents a specific functionality of the product "
    "described in the specification. \n"
    "Features are defined by grouping related user stories. \n"
    "Tasks are defined for each story and represent the engineering "
    "work required to develop the product. \n"
    "A development Plan for a product contains all these components"
)
# TODO: 4 - Instantiate an action_planning_agent using the 'knowledge_action_planning'
action_planning_agent = base_agents.ActionPlanningAgent(
    base_url=base_url,
    openai_api_key=openai_api_key,
    knowledge=knowledge_action_planning
)

# Product Manager - Knowledge Augmented Prompt Agent
persona_product_manager = "You are a Product Manager, you are responsible for defining the user stories for a product."
knowledge_product_manager = (
    "Stories are defined by writing sentences with a persona, an action, and a desired outcome. "
    "The sentences always start with: As a "
    "Write several stories for the product spec below, where the personas are the different users of the product. "
    # TODO: 5 - Complete this knowledge string by appending the product_spec loaded in TODO 3
    + product_spec
)
# TODO: 6 - Instantiate a product_manager_knowledge_agent using 'persona_product_manager' and the completed 'knowledge_product_manager'
product_manager_knowledge_agent = base_agents.KnowledgeAugmentedPromptAgent(
    base_url=base_url,
    openai_api_key=openai_api_key,
    persona=persona_product_manager,
    knowledge=knowledge_product_manager
)

# Product Manager - Evaluation Agent
# TODO: 7 - Define the persona and evaluation criteria for a Product Manager evaluation agent and instantiate it as product_manager_evaluation_agent. This agent will evaluate the product_manager_knowledge_agent.
# The evaluation_criteria should specify the expected structure for user stories (e.g., "As a [type of user], I want [an action or feature] so that [benefit/value].").
persona_product_manager_eval = "You are an evaluation agent that checks the answers of other worker agents."
evaluation_criteria_product_manager = (
    "The answer should be user stories that follow the structure: "
    "As a [type of user], I want [an action or feature] so that [benefit/value]."
)
product_manager_evaluation_agent = base_agents. EvaluationAgent(
    base_url=base_url,
    openai_api_key=openai_api_key,
    persona=persona_product_manager_eval,
    evaluation_criteria=evaluation_criteria_product_manager,
    worker_agent=product_manager_knowledge_agent,
    max_interactions=10
)

# Program Manager - Knowledge Augmented Prompt Agent
persona_program_manager = "You are a Program Manager, you are responsible for defining the features for a product."
knowledge_program_manager = "Features of a product are defined by organizing similar user stories into cohesive groups."
# Instantiate a program_manager_knowledge_agent using 'persona_program_manager' and 'knowledge_program_manager'
# (This is a necessary step before TODO 8. Students should add the instantiation code here.)
program_manager_knowledge_agent = base_agents.KnowledgeAugmentedPromptAgent(
    base_url=base_url,
    openai_api_key=openai_api_key,
    persona=persona_program_manager,
    knowledge=knowledge_program_manager
)

# Program Manager - Evaluation Agent
persona_program_manager_eval = "You are an evaluation agent that checks the answers of other worker agents."
evaluation_criteria_program_manager = (
    "The answer should be product features that follow the following structure: "
    "Feature Name: A clear, concise title that identifies the capability \n"
    "Description: A brief explanation of what the feature does and its purpose \n"
    "Key Functionality: The specific capabilities or actions the feature provides \n"
    "User Benefit: How this feature creates value for the user"
)
# TODO: 8 - Instantiate a program_manager_evaluation_agent using 'persona_program_manager_eval' and the evaluation criteria below.
#                      "The answer should be product features that follow the following structure: " \
#                      "Feature Name: A clear, concise title that identifies the capability\n" \
#                      "Description: A brief explanation of what the feature does and its purpose\n" \
#                      "Key Functionality: The specific capabilities or actions the feature provides\n" \
#                      "User Benefit: How this feature creates value for the user"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.
program_manager_evaluation_agent = base_agents.EvaluationAgent(
    base_url=base_url,
    openai_api_key=openai_api_key,
    persona=persona_program_manager_eval,
    evaluation_criteria=evaluation_criteria_program_manager,
    worker_agent=program_manager_knowledge_agent,
    max_interactions=10
)       

# Development Engineer - Knowledge Augmented Prompt Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining the development tasks for a product."
knowledge_dev_engineer = "Development tasks are defined by identifying what needs to be built to implement each user story."
# Instantiate a development_engineer_knowledge_agent using 'persona_dev_engineer' and 'knowledge_dev_engineer'
# (This is a necessary step before TODO 9. Students should add the instantiation code here.)
development_engineer_knowledge_agent = base_agents.KnowledgeAugmentedPromptAgent(
    base_url=base_url,
    openai_api_key=openai_api_key,
    persona=persona_dev_engineer,
    knowledge=knowledge_dev_engineer
)

# Development Engineer - Evaluation Agent
persona_dev_engineer_eval = "You are an evaluation agent that checks the answers of other worker agents."
evaluation_criteria_dev_engineer = (
    "The answer should be tasks following this exact structure: "
    "Task ID: A unique identifier for tracking purposes \n"
    "Task Title: Brief description of the specific development work \n"
    "Related User Story: Reference to the parent user story \n"
    "Description: Detailed explanation of the technical work required \n"
    "Acceptance Criteria: Specific requirements that must be met for completion \n"
    "Estimated Effort: Time or complexity estimation \n"
    "Dependencies: Any tasks that must be completed first"
)
# TODO: 9 - Instantiate a development_engineer_evaluation_agent using 'persona_dev_engineer_eval' and the evaluation criteria below.
#                      "The answer should be tasks following this exact structure: " \
#                      "Task ID: A unique identifier for tracking purposes\n" \
#                      "Task Title: Brief description of the specific development work\n" \
#                      "Related User Story: Reference to the parent user story\n" \
#                      "Description: Detailed explanation of the technical work required\n" \
#                      "Acceptance Criteria: Specific requirements that must be met for completion\n" \
#                      "Estimated Effort: Time or complexity estimation\n" \
#                      "Dependencies: Any tasks that must be completed first"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.
development_engineer_evaluation_agent = base_agents.EvaluationAgent(
    base_url=base_url,
    openai_api_key=openai_api_key,
    persona=persona_dev_engineer_eval,
    evaluation_criteria=evaluation_criteria_dev_engineer,
    worker_agent=development_engineer_knowledge_agent,
    max_interactions=10
)

# Routing Agent
# TODO: 10 - Instantiate a routing_agent. You will need to define a list of agent dictionaries (routes) for Product Manager, Program Manager, and Development Engineer. Each dictionary should contain 'name', 'description', and 'func' (linking to a support function). Assign this list to the routing_agent's 'agents' attribute.
agents = [
    {
        "name": "Product Manager Agent",
        "description": "This agent defines user stories for the product based on the product specification.",
        "func": lambda x: product_manager_knowledge_agent.respond(x)
    },
    {
        "name": "Program Manager Agent",
        "description": "This agent defines product features by organizing related user stories into cohesive groups.",
        "func": lambda x: program_manager_knowledge_agent.respond(x)
    },
    {
        "name": "Development Engineer Agent",
        "description": "This agent defines development tasks by identifying the technical work required to implement each user story.",
        "func": lambda x: development_engineer_knowledge_agent.respond(x)
    }
]
routing_agent = base_agents.RoutingAgent(
    base_url=base_url,
    openai_api_key=openai_api_key,
    agents=agents
)


# Job function persona support functions
# TODO: 11 - Define the support functions for the routes of the routing agent (e.g., product_manager_support_function, program_manager_support_function, development_engineer_support_function).
# Each support function should:
#   1. Take the input query (e.g., a step from the action plan).
#   2. Get a response from the respective Knowledge Augmented Prompt Agent.
#   3. Have the response evaluated by the corresponding Evaluation Agent.
#   4. Return the final validated response.

def product_manager_support_function(query):
    response = product_manager_knowledge_agent.respond(query)
    evaluation = product_manager_evaluation_agent.evaluate(response)
    return evaluation["final_response"]

def program_manager_support_function(query):
    response = program_manager_knowledge_agent.respond(query)
    evaluation = program_manager_evaluation_agent.evaluate(response)
    return evaluation["final_response"]

def development_engineer_support_function(query):
    response = development_engineer_knowledge_agent.respond(query)
    evaluation = development_engineer_evaluation_agent.evaluate(response)
    return evaluation["final_response"]

# Run the workflow

print("\n*** Workflow execution started ***\n")
# Workflow Prompt
# ****
workflow_prompt = "Create a comprehensive project plan including: " \
"1) user stories for the product, " \
"2) product features organized by capability, " \
"3) development tasks with technical details for each user story"
# ****
print(f"Task to complete in this workflow, workflow prompt = {workflow_prompt}")
 
print("\nDefining workflow steps from the workflow prompt")
# TODO: 12 - Implement the workflow.
#   1. Use the 'action_planning_agent' to extract steps from the 'workflow_prompt'.
#   2. Initialize an empty list to store 'completed_steps'.
#   3. Loop through the extracted workflow steps:
#      a. For each step, use the 'routing_agent' to route the step to the appropriate support function.
#      b. Append the result to 'completed_steps'.
#      c. Print information about the step being executed and its result.
#   4. After the loop, print the final output of the workflow (the last completed step).

# Step 1: Extract steps from the workflow prompt using the action planning agent
workflow_steps = action_planning_agent.extract_steps_from_prompt(workflow_prompt)
#print("Extracted workflow steps:")
#for idx, step in enumerate(workflow_steps):
#    print(f"Step {idx+1}: {step}")
completed_steps = []
step_descriptions = []
for step in workflow_steps:
    print(f"\nExecuting step: {step}")
    # Step 2: Route the step to the appropriate support function using the routing agent
    result = routing_agent.route(step)
    completed_steps.append(result)
    step_descriptions.append(step)
    print(f"Result of step: {result}")

print("\n*** Workflow execution completed ***\n")

# Consolidate all outputs into a comprehensive structured project plan
print("="*80)
print("COMPREHENSIVE PROJECT PLAN - EMAIL ROUTER")
print("="*80)

consolidated_output = "\n" + "="*80 + "\n"
consolidated_output += "COMPREHENSIVE PROJECT PLAN - EMAIL ROUTER\n"
consolidated_output += "="*80 + "\n\n"

# Add all completed steps to the output
for idx, (description, result) in enumerate(zip(step_descriptions, completed_steps)):
    if idx == 0:
        consolidated_output += "USER STORIES\n"
        consolidated_output += "-" * 80 + "\n"
    elif idx == 1:
        consolidated_output += "\nPRODUCT FEATURES\n"
        consolidated_output += "-" * 80 + "\n"
    elif idx == 2:
        consolidated_output += "\nDEVELOPMENT TASKS\n"
        consolidated_output += "-" * 80 + "\n"
    
    consolidated_output += result + "\n"

consolidated_output += "\n" + "="*80 + "\n"

print(consolidated_output)
print(f"Final output of the workflow:\n{consolidated_output}")
