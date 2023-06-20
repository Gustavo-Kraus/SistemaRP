import streamlit as st
import controllers.ClienteController as ClienteController
st.set_page_config(layout="wide")

st.title('Clientes')

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

# Configurações de paginação
registros_por_pagina = 10
total_registros = len(clientes)
total_paginas = (total_registros - 1) // registros_por_pagina + 1

# Navegação entre páginas
pagina_atual = st.selectbox('Página', range(1, total_paginas + 1), index=0, key='pagina_atual')
inicio = (pagina_atual - 1) * registros_por_pagina
fim = inicio + registros_por_pagina

# Exibição dos registros da página atual
for x, item in enumerate(clientes[inicio:fim]):
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns((1, 5, 4, 2, 2, 2, 2, 2))
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

    if on_click_alterar:
        st.experimental_set_query_params(id=item.id)
