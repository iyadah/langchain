import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
os.environ['OPENAI_API_KEY']='sk-xx'
os.environ['SERPAPI_API_KEY']='xx'
print(os.environ['OPENAI_API_KEY'])
print(os.environ['SERPAPI_API_KEY'])
llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
agent.run("who is the current leader of the US and what is the largest prime number that is lower than his age")
