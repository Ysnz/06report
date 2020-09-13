import pandas as pd
import streamlit as st
df = pd.read_csv("https://docs.google.com/spreadsheets/d/1cgAK91V_EgYoFGhMznmI3E7MgJNbIX5bWniSDgRhMq0/export?format=csv&gid=0",
                 index_col="Student Number")
st.title('Student Report')
df[df.index == st.text_input("Enter your student number: ")].T
