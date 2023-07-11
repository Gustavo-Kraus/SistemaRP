import streamlit as st
import controllers.FornecedoresController as FornecedorController
import models.Fornecedor_Consulta as fornecedor_consulta
import pages.Fornecedores.CadastrarFornecedores as CadastrarFornecedor

def Consultar():
    st.title('Fornecedores')
    button_space_cadastrar = st.empty()
    button_id_cadastrar = 'btnCadastrar'
    on_click_cadastrar = button_space_cadastrar.button('Cadastrar', key=button_id_cadastrar)
    if on_click_cadastrar:
        CadastrarFornecedor.cadastrar()
    else:
        paraiD = st.experimental_get_query_params()
    if paraiD == {}:
        pesquisa = st.text_input('Pesquise')

        registros = FornecedorController.SelecionarTodos()
        if pesquisa:
            registros = [fornecedores for fornecedores in registros if
                        pesquisa.lower() in str(fornecedores.id).lower() or
                        pesquisa.lower() in str(fornecedores.cpf).lower() or
                        pesquisa.lower() in fornecedores.nome.lower() or
                        pesquisa.lower() in fornecedores.fantasia.lower() or
                        pesquisa.lower() in fornecedores.rgie.lower() or
                        pesquisa.lower() in fornecedores.email.lower()]
        registros_por_pagina = 10
        total_registros = len(registros)
        total_paginas = (total_registros - 1) // registros_por_pagina + 1

        # Navegação entre páginas
        pagina_atual = st.selectbox('Página', range(1, total_paginas + 1), index=0, key='pagina_atual')
        inicio = (pagina_atual - 1) * registros_por_pagina
        fim = inicio + registros_por_pagina

        colms = st.columns((1, 5, 4, 2, 2, 2, 1.5, 1.5))
        campos = ['Id', 'CPF/CNPJ', 'Nome', 'Nome Fantasia', 'RG/IE', 'Email', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)
        
        for x, item in enumerate(registros[inicio:fim]):
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
                on_click_excluir = button_space_excluir.button('Excluído!!')
                st.experimental_rerun()
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=item.id
                )
                st.experimental_rerun() 
    else:
         CadastrarFornecedor.cadastrar()