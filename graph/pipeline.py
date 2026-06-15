from typing import TypedDict
from langgraph.graph import StateGraph, END
from agents.search_agent import search_agent
from agents.summarizer_agent import summarize
from agents.report_writer import write_report


class ResearchState(TypedDict):
    topic: str
    search_results: list
    summaries: list
    final_report: str

# Node 1 — Search
def search_node(state: ResearchState) -> ResearchState:
    results = search_agent.invoke({"query": state["topic"]})
    return {"search_results": results}

# Node 2 — Summarize
def summarize_node(state: ResearchState) -> ResearchState:
    summaries = []
    for r in state["search_results"]:
        summary = summarize(topic=state["topic"], content=r["content"])
        summaries.append(summary)
    return {"summaries": summaries}

# Node 3 — Report
def report_node(state: ResearchState) -> ResearchState:
    report = write_report(topic=state["topic"], summaries=state["summaries"])
    return {"final_report": report}

# Graph banana
graph = StateGraph(ResearchState)

graph.add_node("search", search_node)
graph.add_node("summarize", summarize_node)
graph.add_node("report", report_node)

graph.set_entry_point("search")
graph.add_edge("search", "summarize")
graph.add_edge("summarize", "report")
graph.add_edge("report", END)

pipeline = graph.compile()
