import os
from langchain.llms import OpenAI
os.environ['OPENAI_API_KEY']='sk-xxxx'
print(os.environ['OPENAI_API_KEY'])
llm = OpenAI(temperature=0.9)
text = "What are 5 vacation destinations for someone who likes to eat meat"
print(llm(text))
