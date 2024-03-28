import openai  
from langchain.llms import OpenAI
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import time
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

open_api_key= os.environ.get("OPENAI_AI_KEY")
llm=OpenAI(openai_api_key=open_api_key)

cities = ['Karachi',
          'Islamabad',
          'Lahore',
          'Faisalabad',
          'Sialkot',
          'Murree',
          'Rawalpindi',]

prompt= PromptTemplate.from_template("what is the capital of {place}")
#print(llm.predict("what is the capital of pakistan"))
llm=OpenAI(temperature=0.3)

chain=LLMChain(llm=llm,prompt=prompt)
for city in cities:
    output=chain.run(city)
    print(output)
    time.sleep(2)
print(os.getenv("OPENAI_API_KEY"))
print("We ok")