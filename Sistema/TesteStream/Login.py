import streamlit as st
import pandas as pd
from json import loads
from pandas import read_csv
from pandas import read_excel

st.title('*Olá, seja muito bem vindo*')
st.write('Coloque sua credenciais')



Email = st.text_input('Email', max_chars=30, placeholder='Coloque seu email',)
Senha = st.text_input('Senha', type='password', max_chars=12, placeholder='Máximo 12 caracteres')

st.button('Acessar')


