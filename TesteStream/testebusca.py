import streamlit as st
import pandas as pd


text_search = st.text_input("Search videos by title or speaker", value="")

m1 = df["Autor"].str.contains(text_search)
m2 = df["Título"].str.contains(text_search)
df_search = df[m1 | m2]