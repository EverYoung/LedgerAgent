from google.adk.agents import LoopAgent, LlmAgent, SequentialAgent
from google.adk.tools.tool_context import ToolContext
from . import prompts

# --- Tool Definition ---
def exit_loop(tool_context: ToolContext):
  """Call this function ONLY when the reviwer indicates all the transactions are recorded and correct."""
  print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
  tool_context.actions.escalate = True
  # Return empty dict as tools should typically return JSON-serializable output
  return {}


# --- Agent Definition ---
statement_parser_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="StatementParser",
    description="As an accountant, look at all transactions in statement files and record transactions in a specific format.",
    instruction=prompts.statement_parser_prompt,
)

statement_reviewer_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="StatementReviewer",
    description="As a manager, compare all the recorded transactions with the original statement files and check if all transactions are recorded with correct information.",
    instruction=prompts.statement_reviewer_prompt,
    tools=[exit_loop]
)

transaction_recording_agent = LoopAgent(
    name="StatementRecordingLoop",
    max_iterations=5,
    sub_agents=[statement_parser_agent, statement_reviewer_agent]
)

format_refiner = LlmAgent(
    model="gemini-2.5-flash",
    name="FormatRefiner",
    description="An agent that is good at converting data in a random format into the a specific format",
    instruction=prompts.format_refiner_prompt,
)

sequantial_agent = SequentialAgent(
    name='StatementParsingAgent',
    sub_agents=[transaction_recording_agent, format_refiner]
)
