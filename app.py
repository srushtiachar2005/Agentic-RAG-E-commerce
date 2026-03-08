import streamlit as st
from workflow import workflow

st.title("Agentic AI Shopping Assistant")

query = st.text_input("Ask something")

if st.button("Submit"):

    result = workflow.invoke({"query":query})

    st.write(result["result"])