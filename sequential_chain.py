import openai  
from langchain.llms import OpenAI
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import time
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

open_api_key= os.environ.get("OPENAI_AI_KEY")
llm=OpenAI(openai_api_key=open_api_key)

llm = OpenAI(temperature=0.7)
template = """You are a playwright. Given the title of play, it is your job to write a synopsis for that title.
Title: {title}
Era: {era}
Playwright: This is a synopsis for the above play:"""
prompt_t = PromptTemplate(template=template, input_variables=["title", "era"])
sypnosis_chain = LLMChain(llm=llm, prompt=prompt_t, output_key="sypnosis")

llm = OpenAI(temperature=0.7)
template = """You are a play critic from the New York Times. Given the sypnosis of play, it is your job to come up with a positive review of the play.
Play Sypnosis:
{sypnosis}
Review from a New York Times play critic of the above play:"""
prompt_t = PromptTemplate(input_variables=["sypnosis"], template=template)
review_chain = LLMChain(llm=llm, prompt=prompt_t, output_key="review")

overall_chain = SequentialChain(chains=[sypnosis_chain, review_chain],
                                input_variables=["era", "title"],
                                output_variables=["sypnosis", "review"],
                                verbose=True)

print(overall_chain({"era": "Renaissance", "title": "Tragedy of Hamlet"}))