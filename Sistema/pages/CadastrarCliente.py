import streamlit as st
import controllers.ClienteController as ClienteController
import models.Cliente as clientes
import pandas as pd





def cadastrar():

    idAlteração = st.experimental_get_query_params()
    st.experimental_set_query_params()
    if idAlteração.get("id") !=None:
          idAlteração = idAlteração.get("id")[0]
          st.write(idAlteração)
          st.title('Editar Cliente')
    else:
          st.title('Cadastrar Cliente')
    with st.form(key="Cliente"):
            st.subheader('Geral')
            input_cfp_cnpj_cliente = st.text_input(label="CPF/CNPJ *",placeholder="123.123.123-00")
            input_nome_cliente = st.text_input(label="Nome/Razão Social")
            input_nome_fantasia_cliente = st.text_input(label="Nome Fantasia")
            input_rg_ie_cliente = st.text_input(label="RG/IE")
            st.subheader('Endereço')
            input_cep_cliente = st.text_input(label="CEP",placeholder="12345-123")
            input_uf_cliente = st.text_input(label="UF", placeholder="SC")
            input_municipio_cliente = st.text_input(label="Municipio")
            input_rua_cliente = st.text_input(label="Rua")
            input_numero_endereco_cliente = st.text_input(label="Numero")
            input_bairro_cliente = st.text_input(label="Bairro")
            input_complemento_cliente = st.text_input(label="Complemento")
            st.subheader("Contato")
            input_email_cliente = st.text_input(label="Email")
            input_celular_cliente = st.text_input(label="Celular")
            input_telefone_cliente = st.text_input(label="Telefone")
            input_button_submit = st.form_submit_button("Cadastrar")
    if input_button_submit:
            ultimoid = ClienteController.ultimomaisum()
            clientes.id = ultimoid
            clientes.cpf = input_cfp_cnpj_cliente
            clientes.nome = input_nome_cliente
            clientes.fantasia = input_nome_fantasia_cliente
            clientes.rgie = input_rg_ie_cliente
            clientes.cep = input_cep_cliente
            clientes.uf = input_uf_cliente
            clientes.municipio = input_municipio_cliente
            clientes.rua = input_rua_cliente
            clientes.numero = input_numero_endereco_cliente
            clientes.bairro = input_bairro_cliente
            clientes.complemento = input_complemento_cliente
            clientes.email = input_email_cliente
            clientes.celular = input_celular_cliente
            clientes.telefone = input_telefone_cliente
            ClienteController.Incluir(clientes)
            st.success("Cliente incluido com sucesso!")
    
        