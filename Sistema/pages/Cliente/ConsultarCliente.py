import streamlit as st
import controllers.ClienteController as ClienteController
import pages.Cliente.CadastrarCliente as CadastrarCliente

def ConsultarCliente():
    st.title('Clientes')
    button_space_cadastrar = st.empty()
    button_id_cadastrar = 'btnCadastrar'
    on_click_cadastrar = button_space_cadastrar.button('Cadastrar', key=button_id_cadastrar)
    if on_click_cadastrar:
        CadastrarCliente.cadastrar()
    else:
        paraiD = st.experimental_get_query_params()
    if paraiD == {}:
        # Campo de busca na barra lateral
        pesquisa = st.text_input('Pesquisar por nome, CPF, ID, etc.')
        # Filtrar a lista de clientes com base na pesquisa
        clientes = ClienteController.SelecionarTodos()
        if pesquisa:
            clientes = [cliente for cliente in clientes if
                        pesquisa.lower() in str(cliente.id).lower() or
                        pesquisa.lower() in str(cliente.cpf).lower() or
                        pesquisa.lower() in cliente.nome.lower() or
                        pesquisa.lower() in cliente.fantasia.lower() or
                        pesquisa.lower() in cliente.rgie.lower() or
                        pesquisa.lower() in cliente.email.lower()]

        if len(clientes) == 0:
            st.warning("Nenhum cliente encontrado.")
            return

        # Configurações de paginação
        registros_por_pagina = 10
        total_registros = len(clientes)
        total_paginas = (total_registros - 1) // registros_por_pagina + 1

        # Navegação entre páginas
        pagina_atual = st.selectbox('Página', range(1, total_paginas + 1), index=0, key='pagina_atual')
        inicio = (pagina_atual - 1) * registros_por_pagina
        fim = inicio + registros_por_pagina

        # Exibição dos headers
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns((1, 2, 4, 4, 2, 3, 2, 2))
        col1.header("ID")
        col2.header("CPF")
        col3.header("Nome")
        col4.header("Fantasia")
        col5.header("RG/IE")
        col6.header("Email")

        # Exibição dos registros da página atual
        for x, item in enumerate(clientes[inicio:fim]):
            col1, col2, col3, col4, col5, col6, col7, col8 = st.columns((1, 2, 4, 4, 2, 3, 2, 2))
            col1.write(str(item.id))
            col2.write(item.cpf)
            col3.write(item.nome)
            col4.write(item.fantasia)
            col5.write(item.rgie)
            col6.write(item.email)
            button_space_excluir = col7.empty()
            button_id_excluir = 'btnExcluir' + str(item.id)
            on_click_excluir = button_space_excluir.button('Excluir', key=button_id_excluir)
            button_space_alterar = col8.empty()
            button_id_alterar = 'btnAlterar' + str(item.id)
            on_click_alterar = button_space_alterar.button('Alterar', key=button_id_alterar)
            

            if on_click_excluir:
                ClienteController.excluir(item.id)
                button_id_excluir = 'btnExcluir'
                on_click_excluir = button_space_excluir.button('Excluído!!')
                st.experimental_rerun()
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=item.id
                )
                st.experimental_rerun()
            
    else:
        CadastrarCliente.cadastrar()
