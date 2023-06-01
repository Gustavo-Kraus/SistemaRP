from os import write
from numpy.core.fromnumeric import size
import streamlit as st
import controllers.ClienteController as ClienteController
import models.Cliente as clientes
import pandas as pd
import pages.Cliente.CadastrarCliente as PageCadastrarCliente
import pages.Cliente.ConsultarCliente as PageConsultarCliente
import pages.Produtos.CadastrarProdutos as PageCadastrarProdutos
import pages.Produtos.ConsultarProdutos as PageConsultarProdutos
import pages.Fornecedores.CadastrarFornecedores as PageCadastrarFornecedor
import pages.Fornecedores.ConsultarFornecedores as PageConsultarFornecedor


st.set_page_config(layout="wide")


bar = st.sidebar

container = st.container()
a, b, c = container.columns(3)



clientess = bar.selectbox(
    'Cadastro Cliente',
    ['','Cadastrar Cliente', 'Consultar Clientes', 'Alterar Clientes', 'Excluir Clientes']
)

produtos = bar.selectbox(
    'Cadastro Produto',
    ['','Cadastrar Produto', 'Consultar Produtos', 'Alterar Produtos', 'Excluir Produtos']
)

fornecedoress = bar.selectbox(
    'Cadastro Fornecedor',
    ['','Cadastrar Fornecedor', 'Consultar Fornecedor', 'Alterar Fornecedor', 'Excluir Fornecedor']
)
 



if clientess == 'Consultar Clientes':
    PageConsultarCliente.list()
    


if clientess == 'Cadastrar Cliente':
    PageCadastrarCliente.cadastrar()


if produtos == 'Cadastrar Produto':
    PageCadastrarProdutos.cadastrar()


if produtos == 'Consultar Produtos':
    PageConsultarProdutos.consultar()


if fornecedoress == 'Consultar Fornecedor':
    PageConsultarFornecedor.consultar()


if fornecedoress == 'Cadastrar Fornecedor':
    PageCadastrarFornecedor.cadastrar()




