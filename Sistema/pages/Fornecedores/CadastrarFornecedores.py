import streamlit as st
import controllers.FornecedoresController as FornecedorController
import models.Fornecedores as fornecedor_model  # Renomeie o módulo

def cadastrar():
        idAlteração = st.experimental_get_query_params()
        st.experimental_set_query_params()
        fornecedorRecuperado = None    

        if idAlteração.get("id") is not None:
                idAlteração = idAlteração.get("id")[0]
                fornecedorRecuperado = FornecedorController.SelecionarById(idAlteração)
                st.experimental_set_query_params(id=[fornecedorRecuperado.id])
        else:
                st.title('Cadastrar Fornecedor')
        with st.form(key="Fornecedores"):
                if fornecedorRecuperado is None:
                                st.subheader('Geral')
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
                else:
                                input_cfp_cnpj_fornecedor = st.text_input(label="CPF/CNPJ *", value=fornecedorRecuperado.cpf)
                                input_nome = st.text_input(label="Nome/Razão Social", value=fornecedorRecuperado.nome)
                                input_nome_fantasia_fornecedor = st.text_input(label="Nome Fantasia", value=fornecedorRecuperado.fantasia)
                                input_rg_ie_fornecedor = st.text_input(label="RG/IE", value=fornecedorRecuperado.rgie)
                                st.subheader('Endereço')
                                input_cep_fornecedor = st.text_input(label="CEP", placeholder="12345-123", value=fornecedorRecuperado.cep)
                                input_uf_fornecedor = st.text_input(label="UF", placeholder="SC", value=fornecedorRecuperado.uf)
                                input_municipio_fornecedor = st.text_input(label="Município", value=fornecedorRecuperado.municipio)
                                input_rua_fornecedor = st.text_input(label="Rua", value=fornecedorRecuperado.rua)
                                input_numero_endereco_fornecedor = st.text_input(label="Número", value=fornecedorRecuperado.numero)
                                input_bairro_fornecedor = st.text_input(label="Bairro", value=fornecedorRecuperado.bairro)
                                input_complemento_fornecedor = st.text_input(label="Complemento", value=fornecedorRecuperado.complemento)
                                st.subheader("Contato")
                                input_email_fornecedor = st.text_input(label="Email", value=fornecedorRecuperado.email)
                                input_celular_fornecedor = st.text_input(label="Celular", value=fornecedorRecuperado.celular)
                                input_telefone_fornecedor = st.text_input(label="Telefone", value=fornecedorRecuperado.telefone)

                input_button_submit = st.form_submit_button("Cadastrar/Alterar")
                
                if input_button_submit:
                        if fornecedorRecuperado is None:
                                FornecedorController.IncluirFornecedores(
                                        fornecedor_model.Fornecedores(  # Usar o nome fornecedor_model
                                                FornecedorController.ultimomaisum(),
                                                input_cfp_cnpj_fornecedor,
                                                input_nome,
                                                input_nome_fantasia_fornecedor,
                                                input_rg_ie_fornecedor,
                                                input_cep_fornecedor,
                                                input_uf_fornecedor,
                                                input_municipio_fornecedor,
                                                input_rua_fornecedor,
                                                input_numero_endereco_fornecedor,
                                                input_bairro_fornecedor,
                                                input_complemento_fornecedor,
                                                input_email_fornecedor,
                                                input_celular_fornecedor,
                                                input_telefone_fornecedor))
                                st.success("Fornecedor incluido com sucesso!")
                        else:
                                st.experimental_set_query_params()
                                FornecedorController.Alterar(
                                        fornecedor_model.Fornecedores(  # Usar o nome fornecedor_model
                                                fornecedorRecuperado.id,
                                                input_cfp_cnpj_fornecedor,
                                                input_nome,
                                                input_nome_fantasia_fornecedor,
                                                input_rg_ie_fornecedor,
                                                input_cep_fornecedor,
                                                input_uf_fornecedor,
                                                input_municipio_fornecedor,
                                                input_rua_fornecedor,
                                                input_numero_endereco_fornecedor,
                                                input_bairro_fornecedor,
                                                input_complemento_fornecedor,
                                                input_email_fornecedor,
                                                input_celular_fornecedor,
                                                input_telefone_fornecedor))
                                
                                st.success("Fornecedor alterado com sucesso!")
