import streamlit as st
import controllers.ClienteController as ClienteController
import models.Cliente as clientes

def cadastrar():
    idAlteração = st.experimental_get_query_params()
    st.experimental_set_query_params()
    clienteRecuperado = None

    if idAlteração.get("id") is not None:
        idAlteração = idAlteração.get("id")[0]
        clienteRecuperado = ClienteController.SelecionarById(idAlteração)
        st.experimental_set_query_params(id=[clienteRecuperado.id])
        st.title('Editar Cliente')
    else:
        st.title('Cadastrar Cliente')

    with st.form(key="Cliente"):
        if clienteRecuperado is None:
            st.subheader('Geral')
            input_cpf_cnpj_cliente = st.text_input(label="CPF/CNPJ *", placeholder="123.123.123-00")
            input_nome_cliente = st.text_input(label="Nome/Razão Social")
            input_nome_fantasia_cliente = st.text_input(label="Nome Fantasia")
            input_rg_ie_cliente = st.text_input(label="RG/IE")
            st.subheader('Endereço')
            input_cep_cliente = st.text_input(label="CEP", placeholder="12345-123")
            input_uf_cliente = st.text_input(label="UF", placeholder="SC")
            input_municipio_cliente = st.text_input(label="Município")
            input_rua_cliente = st.text_input(label="Rua")
            input_numero_endereco_cliente = st.text_input(label="Número")
            input_bairro_cliente = st.text_input(label="Bairro")
            input_complemento_cliente = st.text_input(label="Complemento")
            st.subheader("Contato")
            input_email_cliente = st.text_input(label="Email")
            input_celular_cliente = st.text_input(label="Celular")
            input_telefone_cliente = st.text_input(label="Telefone")
            teste = st.text_input
        else:
            input_cpf_cnpj_cliente = st.text_input(label="CPF/CNPJ *", value=clienteRecuperado.cpf)
            input_nome_cliente = st.text_input(label="Nome/Razão Social", value=clienteRecuperado.nome)
            input_nome_fantasia_cliente = st.text_input(label="Nome Fantasia", value=clienteRecuperado.fantasia)
            input_rg_ie_cliente = st.text_input(label="RG/IE", value=clienteRecuperado.rgie)
            st.subheader('Endereço')
            input_cep_cliente = st.text_input(label="CEP", placeholder="12345-123", value=clienteRecuperado.cep)
            input_uf_cliente = st.text_input(label="UF", placeholder="SC", value=clienteRecuperado.uf)
            input_municipio_cliente = st.text_input(label="Município", value=clienteRecuperado.municipio)
            input_rua_cliente = st.text_input(label="Rua", value=clienteRecuperado.rua)
            input_numero_endereco_cliente = st.text_input(label="Número", value=clienteRecuperado.numero)
            input_bairro_cliente = st.text_input(label="Bairro", value=clienteRecuperado.bairro)
            input_complemento_cliente = st.text_input(label="Complemento", value=clienteRecuperado.complemento)
            st.subheader("Contato")
            input_email_cliente = st.text_input(label="Email", value=clienteRecuperado.email)
            input_celular_cliente = st.text_input(label="Celular", value=clienteRecuperado.celular)
            input_telefone_cliente = st.text_input(label="Telefone", value=clienteRecuperado.telefone)

        input_button_submit = st.form_submit_button("Cadastrar/Alterar")

    if input_button_submit:
        if clienteRecuperado is None:
            ClienteController.Incluir(
                clientes.Cliente(
                    ClienteController.ultimomaisum(),
                    input_cpf_cnpj_cliente,
                    input_nome_cliente,
                    input_nome_fantasia_cliente,
                    input_rg_ie_cliente,
                    input_cep_cliente,
                    input_uf_cliente,
                    input_municipio_cliente,
                    input_rua_cliente,
                    input_numero_endereco_cliente,
                    input_bairro_cliente,
                    input_complemento_cliente,
                    input_email_cliente,
                    input_celular_cliente,
                    input_telefone_cliente
                )
            )
            st.success("Cliente incluído com sucesso!")
            st.experimental_rerun()
        else:
            st.experimental_set_query_params()
            ClienteController.Alterar(
                clientes.Cliente(
                    clienteRecuperado.id,
                    input_cpf_cnpj_cliente,
                    input_nome_cliente,
                    input_nome_fantasia_cliente,
                    input_rg_ie_cliente,
                    input_cep_cliente,
                    input_uf_cliente,
                    input_municipio_cliente,
                    input_rua_cliente,
                    input_numero_endereco_cliente,
                    input_bairro_cliente,
                    input_complemento_cliente,
                    input_email_cliente,
                    input_celular_cliente,
                    input_telefone_cliente
                )
            )
            st.success("Cliente alterado com sucesso!")



            