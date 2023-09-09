import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
os.environ['OPENAI_API_KEY']='sk-xx'
print(os.environ['OPENAI_API_KEY'])
llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(input_variables=['food'], template="What are 5 vacation destinations for someone who likes to eat {food}",)
print(prompt.format(food="desert"))
print(llm(prompt.format(food="desert")))
