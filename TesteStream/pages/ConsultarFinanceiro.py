import streamlit as st
import controllers.FinanceiroController as FinanceiroController
import controllers.ClienteController as ClienteController
st.set_page_config(layout="wide")

st.title('Consultar Financeiro')

# Campo de busca na barra lateral
pesquisa = st.text_input('Pesquisar por cliente, valor, etc.')

# Filtrar a lista de registros financeiros com base na pesquisa
registros = FinanceiroController.SelecionarTodos()
if pesquisa:
    registros = [registro for registro in registros if
                 pesquisa.lower() in str(registro.id).lower() or
                 pesquisa.lower() in str(registro.client_id_financeiro).lower() or
                 pesquisa.lower() in str(registro.data_registro.strftime("%Y-%m-%d")).lower() or
                 pesquisa.lower() in str(registro.data_validade.strftime("%Y-%m-%d")).lower() or
                 pesquisa.lower() in str(registro.valor).lower() or
                 pesquisa.lower() in str(registro.valor_pago).lower() or
                 pesquisa.lower() in str(ClienteController.ObterNomeCliente(registro.client_id_financeiro)).lower()]


registros_por_pagina = 10
total_registros = len(registros)
total_paginas = (total_registros - 1) // registros_por_pagina + 1

# Navegação entre páginas
pagina_atual = st.selectbox('Página', range(1, total_paginas + 1), index=0, key='pagina_atual')
inicio = (pagina_atual - 1) * registros_por_pagina
fim = inicio + registros_por_pagina

# Exibição dos cabeçalhos
col1, col2, col3, col4, col5, col6, col7 = st.columns((0.4, 2, 1, 2, 2, 1, 1))
for x, item in enumerate(registros[inicio:fim]):
    col1.write(item.id)
    col3.write(item.valor)
    col4.write(item.valor_pago)
    col5.write(item.data_validade.strftime("%Y-%m-%d"))
    # Consulta o ClienteController para obter o nome do cliente
    nome_cliente = ClienteController.ObterNomeCliente(item.client_id_financeiro)
    col2.write(nome_cliente)
    # Verificar se há um registro correspondente antes de exibir os botões
    button_space_excluir = col6.empty()
    button_id_excluir_financeiro = 'btnExcluir' + str(item.id)
    on_click_excluir = button_space_excluir.button('Excluir', key=button_id_excluir_financeiro)
    button_space_alterar = col7.empty()
    button_id_alterar = 'btnAlterar' + str(item.id)
    on_click_alterar = button_space_alterar.button('Alterar', key=button_id_alterar)
    # Lógica para excluir o registro
    if on_click_excluir:
        FinanceiroController.excluir_registro(item.client_id_financeiro)
        st.success("Registro excluído com sucesso!")

    # Lógica para alterar o registro
    if on_click_alterar:
        # Implemente aqui a lógica para alterar o registro
        pass
