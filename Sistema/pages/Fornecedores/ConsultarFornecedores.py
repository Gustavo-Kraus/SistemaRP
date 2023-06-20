import streamlit as st
import controllers.FornecedoresController as FornecedorController
import models.Fornecedor_Consulta as fornecedor_consulta

def list():
    st.title('Fornecedores')
    st.text_input('Pesquise')
    colms = st.columns((1, 5, 4, 2, 2, 2, 1.5, 1.5))
    campos = ['Id', 'CPF/CNPJ', 'Nome', 'Nome Fantasia', 'RG/IE', 'Email', 'Excluir', 'Alterar']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)
    
    for item in FornecedorController.SelecionarTodos():
        col1, col2, col3, col4, col5, col6, cal7, cal8 = st.columns((1, 5, 4, 2, 2, 2, 1.5, 1.5))
        col1.write(item.id)
        col2.write(item.cpf)
        col3.write(item.nome)
        col4.write(item.fantasia)
        col5.write(item.rgie)
        col6.write(item.email)
        button_space_excluir = cal7.empty()
        button_id_excluir = 'btnExcluir' + str(item.id)
        on_click_excluir = button_space_excluir.button('Excluir', key=button_id_excluir)
        button_space_alterar = cal8.empty()
        button_id_alterar = 'btnAlterar' + str(item.id)
        on_click_alterar = button_space_alterar.button('Alterar', key=button_id_alterar)

        if on_click_excluir:
            FornecedorController.excluir(item.id)
            button_id_excluir = 'btnExcluir'
            on_click_excluir = button_space_excluir.button('Excluido!!')
        if on_click_alterar:
            st.experimental_get_query_params(
                    id = [item.id]
            )