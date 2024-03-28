import openai  
from langchain.llms import OpenAI
import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

import time
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

open_api_key= os.environ.get("OPENAI_AI_KEY")
llm=OpenAI(openai_api_key=open_api_key)

#Memory In LLMs
prompt= PromptTemplate.from_template("what is the name of the e commerce store that sells {product}?")
llm=OpenAI(temperature=0.3)
chain=LLMChain(llm=llm,prompt=prompt,memory=ConversationBufferMemory())
output=chain.run("Fruits")
output1=chain.run("Iphone")

#Prints all queries run in this program
print(chain.memory.buffer)

print(output)
print(output1)

