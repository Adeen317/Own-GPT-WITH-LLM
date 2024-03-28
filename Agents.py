import openai  
from langchain.llms import OpenAI
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.agents import AgentType, Agent, Tool, initialize_agent, load_tools
import time
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

open_api_key= os.environ.get("OPENAI_AI_KEY")
llm=OpenAI(openai_api_key=open_api_key)

#Agent Demo
llm=OpenAI(temperature=0.7)
tools=load_tools(["wikipedia","llm-math"],llm=llm)
agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)#,verbose=True)
output = agent.run("how many universities are there in Pakistan,Sindh")
print(output)


