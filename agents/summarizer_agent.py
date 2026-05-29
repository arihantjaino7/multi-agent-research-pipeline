from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research assistant, summmarize the given content concisely"),
    ("human","Topic : {topic}\nContent : {content}")
])

chain = prompt | llm | StrOutputParser()

def summarize(topic: str, content: str) -> str:
    result = chain.invoke({"topic" : topic, "content" : content})
    return str(result)