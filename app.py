import streamlit as st
from graph.pipeline import pipeline
import os

st.title("🔍 Multi-Agent Research Pipeline")
st.write("Enter a topic and get a full research report automatically.")

topic = st.text_input("Research Topic", placeholder="e.g. future of quantum computing")

if st.button("Generate Report"):
    if topic:
        with st.spinner("Researching... this may take a minute..."):
            result = pipeline.invoke({"topic": topic})
            report = result["final_report"]

        st.markdown(report)

        # Save to file
        filename = topic.replace(" ", "_") + ".md"
        filepath = os.path.join("outputs", filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# Research Report: {topic}\n\n")
            f.write(report)

        st.success(f"Report saved: {filepath}")

        st.download_button(
            label="Download Report",
            data=report,
            file_name=filename,
            mime="text/markdown"
        )
    else:
        st.warning("Please enter a topic first.")