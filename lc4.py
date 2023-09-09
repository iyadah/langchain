import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
os.environ['OPENAI_API_KEY']='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'
os.environ['SERPAPI_API_KEY']='5a64aff7c0a40bc5901b01368cd894c90a4e01925f99a1d1bec544c4c977f4df'
print(os.environ['OPENAI_API_KEY'])
print(os.environ['SERPAPI_API_KEY'])
llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
agent.run("who is the current leader of the US and what is the largest prime number that is lower than his age")
