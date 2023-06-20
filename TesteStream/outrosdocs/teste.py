import streamlit as st
import pandas as pd
from json import loads
from pandas import read_csv
from pandas import read_excel
import controllers.ClienteController as ClienteController
import models.Cliente as clientes

with st.form(key="Clientess"):
    st.subheader('Geral')
    input_cfp_cnpj_cliente = st.text_input(label="CPF/CNPJ",placeholder="123.123.123-00")
    input_nome_cliente = st.text_input(label="Nome/Razão Social")
    input_button_submit = st.form_submit_button("Cadastrar")
if input_button_submit:
        clientes.cpf = input_cfp_cnpj_cliente
        clientes.nome = input_nome_cliente
        ClienteController.Incluir(clientes)