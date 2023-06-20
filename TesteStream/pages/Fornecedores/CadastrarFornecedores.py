import streamlit as st
import controllers.FornecedoresController as FornecedorController
import models.Fornecedores as fornecedor
import pandas as pd
def cadastrar():
    for item in FornecedorController.ultimoid():
           id_agora = item.id
           id_soma = 1
           soma = id_agora + id_soma

    st.title('Cadastrar Fornecedor')
    with st.form(key="Fornecedores"):
            st.subheader('Geral')
            input_id = st.number_input(label="id", format="%d", value= soma)
            input_cfp_cnpj_fornecedor = st.text_input(label="CPF/CNPJ",placeholder="123.123.123-00")
            input_nome = st.text_input(label="Nome/Razão Social")
            input_nome_fantasia_fornecedor = st.text_input(label="Nome Fantasia")
            input_rg_ie_fornecedor = st.text_input(label="RG/IE")
            st.subheader('Endereço')
            input_cep_fornecedor = st.text_input(label="CEP",placeholder="12345-123")
            input_uf_fornecedor = st.text_input(label="UF", placeholder="SC")
            input_municipio_fornecedor = st.text_input(label="Municipio")
            input_rua_fornecedor = st.text_input(label="Rua")
            input_numero_endereco_fornecedor = st.text_input(label="Numero")
            input_bairro_fornecedor = st.text_input(label="Bairro")
            input_complemento_fornecedor = st.text_input(label="Complemento")
            st.subheader("Contato")
            input_email_fornecedor = st.text_input(label="Email")
            input_celular_fornecedor = st.text_input(label="Celular")
            input_telefone_fornecedor = st.text_input(label="Telefone")
            input_button_submit = st.form_submit_button("Cadastrar")
    if input_button_submit:
            fornecedor.id = input_id
            fornecedor.cpf = input_cfp_cnpj_fornecedor
            fornecedor.nome = input_nome
            fornecedor.fantasia = input_nome_fantasia_fornecedor
            fornecedor.rgie = input_rg_ie_fornecedor
            fornecedor.cep = input_cep_fornecedor
            fornecedor.uf = input_uf_fornecedor
            fornecedor.municipio = input_municipio_fornecedor
            fornecedor.rua = input_rua_fornecedor
            fornecedor.numero = input_numero_endereco_fornecedor
            fornecedor.bairro = input_bairro_fornecedor
            fornecedor.complemento = input_complemento_fornecedor
            fornecedor.email = input_email_fornecedor
            fornecedor.celular = input_celular_fornecedor
            fornecedor.telefone = input_telefone_fornecedor
            for item in FornecedorController.ultimoid():
             id_agora = item.id
             id_soma = 1
             soma = id_agora + id_soma

            FornecedorController.IncluirFornecedores(fornecedor)
            st.success("Fornecedor incluido com sucesso!")
        
    
    
    
    
    
    
    
