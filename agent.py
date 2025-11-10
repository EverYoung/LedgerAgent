from google.adk.agents import LlmAgent
from . import sub_agents


root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    sub_agents=[sub_agents.sequantial_agent]
)