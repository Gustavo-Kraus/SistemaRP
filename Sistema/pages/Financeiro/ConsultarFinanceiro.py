import streamlit as st
import controllers.FinanceiroController as FinanceiroController
import controllers.ClienteController as ClienteController
import pages.Financeiro.CadastrarFinanceiro as CadastrarFinanceiro
from datetime import date

def ConsultarFinanceiro():
    button_space_cadastrar = st.empty()
    button_id_cadastrar = 'btnCadastrar'
    on_click_cadastrar = button_space_cadastrar.button('Cadastrar', key=button_id_cadastrar)
    if on_click_cadastrar:
        CadastrarFinanceiro.CadastrarFinanceiro()
    else:
        paraiD = st.experimental_get_query_params()
        if paraiD == {}:
            st.title('Consultar Financeiro')
            # Campo de filtro na barra lateral
            filtro = st.selectbox('Filtrar por:', ('Todos', 'Atrasados', 'Vencem Hoje'))

            # Campo de busca na barra lateral
            pesquisa = st.text_input('Pesquisar')

            # Filtrar a lista de registros financeiros com base no filtro selecionado
            registros = FinanceiroController.SelecionarTodos()
            data_atual = date.today()

            if filtro == 'Atrasados':
                registros = [registro for registro in registros if registro.data_validade < data_atual]
            elif filtro == 'Vencem Hoje':
                registros = [registro for registro in registros if registro.data_validade == data_atual]

            # Filtrar a lista de registros com base na pesquisa
            if pesquisa:
                registros = [registro for registro in registros if
                            pesquisa.lower() in str(registro.id).lower() or
                            pesquisa.lower() in str(registro.client_id_financeiro).lower() or
                            pesquisa.lower() in str(registro.data_registro.strftime("%Y/%m/%d")).lower() or
                            pesquisa.lower() in str(registro.data_validade.strftime("%Y/%m/%d")).lower() or
                            pesquisa.lower() in str(registro.valor).lower() or
                            pesquisa.lower() in str(registro.valor_pago).lower() or
                            pesquisa.lower() in str(ClienteController.ObterNomeCliente(registro.client_id_financeiro)).lower()]

            # Restante do código para exibir os registros e interações
            registros_por_pagina = 10
            total_registros = len(registros)
            total_paginas = (total_registros - 1) // registros_por_pagina + 1

            # Navegação entre páginas
            pagina_atual = st.selectbox('Página', range(1, total_paginas + 1), index=0, key='pagina_atual')
            inicio = 0  # Definir o valor padrão para 0

            # Verificar se há registros antes de calcular o valor de início
            if registros:
                inicio = (pagina_atual - 1) * registros_por_pagina

            fim = inicio + registros_por_pagina

            # Exibição dos cabeçalhos
            col1, col2, col3, col4, col5, col6, col7 = st.columns((0.4, 2, 1, 2, 2, 1, 1))
            col1.header("ID")
            col2.header("Nome")
            col3.header("Valor")
            col4.header("Valor Pago")
            col5.header("Validade")
            col6.header("‎")
            col7.header("‎")

            if registros:  # Verificar se há registros para exibir
                for x, item in enumerate(registros[inicio:fim]):
                    col1, col2, col3, col4, col5, col6, col7 = st.columns((0.4, 2, 1, 2, 2, 1, 1))
                    col1.write(str(item.id))
                    col3.write(str(item.valor))  # Converter para string
                    col4.write(str(item.valor_pago))  # Converter para string
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
                        FinanceiroController.excluir_registro(item.id)
                        st.success("Registro excluído com sucesso!")
                        st.experimental_rerun()
                    # Lógica para alterar o registro
                    if on_click_alterar:
                        st.experimental_set_query_params(
                            id=item.id
                        )
                        st.experimental_rerun()
        else:
            CadastrarFinanceiro.CadastrarFinanceiro()

            st.write()
            

