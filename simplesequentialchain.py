import openai  
from langchain.llms import OpenAI
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
import time
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

open_api_key= os.environ.get("OPENAI_AI_KEY")
llm=OpenAI(openai_api_key=open_api_key)



#LLM to get name of an e commerce store from a product name
prompt= PromptTemplate.from_template("what is the name of the e commerce store that sells {product}?")
llm=OpenAI(temperature=0.3)
chain1=LLMChain(llm=llm,prompt=prompt)

#LLM to get comma seperated names of product from an e-commerce store name
prompt= PromptTemplate.from_template("what are the names of the products at {store}?")
llm=OpenAI(temperature=0.3)
chain2=LLMChain(llm=llm,prompt=prompt)

#Create an overall chain from simple sequential chain
chain= SimpleSequentialChain(
  chains=[chain1,chain2], verbose=True
  #input_variables=["product","store"]
)

chain.run("candles")



