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

prompt=ChatPromptTemplate.from_messages([
    ("system","You are professional report writer, write the report for the given data"),
    ("system","""Topic : {topic}
     here are the summaries of 5 different sources: {summaries}
     write a final report wiht : 
     -title
     -executive summary
     - Key findings
     - conclusion""")
])

chain = prompt | llm | StrOutputParser()

def write_report(topic: str, summaries: list) -> str:
    combined_summary = "\n".join(summaries)
    result =  chain.invoke({"topic" : topic, "summaries" : combined_summary})
    return str(result)