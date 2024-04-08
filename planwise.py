import streamlit as st
from datetime import date


st.header('Planewise')

st.caption(
    "Input your project description and deadline, and we'll generate a project plan for you.")

txt = st.text_area(
    "Project Description",
    placeholder="Enter your project description", height=120
    )

today = date.today()
d = st.date_input("Deadline", min_value=today)


submit = st.button("Make Plan", type="primary")
