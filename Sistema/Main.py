from os import write
from numpy.core.fromnumeric import size
import streamlit as st
import controllers.ClienteController as ClienteController
import models.Cliente_Pesquisa as clientes
import pandas as pd
import pages.CadastrarCliente as PageCadastrarCliente
import pages.ConsultarCliente as PageConsultarCliente
import pages.Produtos.CadastrarProdutos as PageCadastrarProdutos
import pages.Produtos.ConsultarProdutos as PageConsultarProdutos
import pages.Fornecedores.CadastrarFornecedores as PageCadastrarFornecedor
import pages.Fornecedores.ConsultarFornecedores as PageConsultarFornecedor
import pages.CadastrarFinanceiro as PageCadastrarFinanceiro
import pages.ConsultarFinanceiro as PageConsultarFinanceiro
import streamlit_authenticator as stauth
import pickle
from pathlib import Path

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Bem Vindo!")

    st.sidebar.success("teste")

if __name__ == "__main__":
    run()

st.set_page_config(layout="wide")

# --- USER AUTHENTICATION ---
nomes = ["Gustavo"]
usernames = ["Gustavo"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_password = pickle.load(file)

authentication = stauth.Authenticate(nomes, usernames, hashed_password,
    "teste", "teste", cookie_expiry_days=5)

nome, authentication_status, username = authentication.login("Login", "main")

def cadastrar():
    for item in ClienteController.todosclientes():
        id_agora = item.id
        
def cadastrar():
    for item in ClienteController.ultimoid():
        ultimo = item.id



if authentication_status == False:
    st.error("Nome ou senha está incorreto")

if authentication_status == nome:
    st.warning("Por favor preencha os campos!")

if authentication_status:
    bar = st.sidebar
    st.sidebar.title(f"Bem vindo {nome}")


'''   container = st.container()
    a = container.columns(1)
    CadastroCliente = bar.selectbox(
        'Clientes',
        ['','Cadastrar Cliente', 'Consultar Clientes']
    )

    container = st.container()
    a = container.columns(1)
    CadastroFinanceiro = bar.selectbox(
        'Financeiro',
        ['','Criar Financeiro', 'Consultar Financeiro']
    )


    if CadastroCliente == 'Cadastrar Cliente':
        PageCadastrarCliente.cadastrar()

    if CadastroCliente == 'Consultar Clientes':
        PageConsultarCliente.list()

    if CadastroFinanceiro == 'Criar Financeiro':
        PageCadastrarFinanceiro.financeiro()

    if CadastroFinanceiro == 'Consultar Financeiro':
        PageConsultarFinanceiro.consultar_financeiro()

    authentication.logout("Deslogar", "sidebar" )
    
'''

