from graph.pipeline import pipeline
import os

topic = "future of quantum computing"

result = pipeline.invoke({"topic": topic})
report = result["final_report"]

print(report)

# outputs folder mein save karo
filename = topic.replace(" ", "_") + ".md"
filepath = os.path.join("outputs", filename)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(f"# Research Report: {topic}\n\n")
    f.write(report)

print(f"\nReport saved: {filepath}")