import streamlit as st
import pandas as pd
from json import loads
from pandas import read_csv
from pandas import read_excel


arquivo = st.file_uploader(
    'Suba Uma Imagem',
    type=['jpg','png', 'py', 'json', 'jpeg', 'csv', 'xlsx']
    
)

if arquivo:
    print(arquivo,type)
    match arquivo.type.split('/'):
        case 'application', 'json':
            st.json(loads(arquivo.read()))
        case 'image', _:
            st.image(arquivo)
        case 'text', 'csv' :
            df = read_csv(arquivo)
            st.dataframe(df)
        case 'xlsx', _:
            x = pd.read_excel(arquivo, engine='openpyxl')
            st.write(x)
else:
    st.error('Ainda não tenho arquivo!')

ont_size = st.number_input ('Tamanho da fonte', min_value=20)
