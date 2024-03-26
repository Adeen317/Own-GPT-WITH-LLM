

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI


llm = ChatOpenAI(openai_api_key="")
llm = OpenAI()
chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125")

from langchain_core.messages import HumanMessage

text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]

llm.invoke(text)
# >> Feetful of Fun

chat_model.invoke(messages)