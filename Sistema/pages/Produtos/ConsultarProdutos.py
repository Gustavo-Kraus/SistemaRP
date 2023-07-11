import streamlit as st
import controllers.ProdutosController as ProdutosController
import models.Produtos as produto
import pages.Produtos.CadastrarProdutos as CadastrarProduto

def consultar():
    button_space_cadastrar = st.empty()
    button_id_cadastrar = 'btnCadastrar'
    on_click_cadastrar = button_space_cadastrar.button('Cadastrar', key=button_id_cadastrar)
    if on_click_cadastrar:
        CadastrarProduto.cadastrar()
    else:
        st.title('Produtos')
        pesquisa = st.text_input('Pesquisar')
        registros = ProdutosController.SelecionarTodos()
        if pesquisa:
                registros = [registro for registro in registros if
                            pesquisa.lower() in str(registro.id).lower() or
                            pesquisa.lower() in str(registro.nome).lower() or
                            pesquisa.lower() in str(registro.barras).lower() or
                            pesquisa.lower() in str(registro.quantidade).lower() or
                            pesquisa.lower() in str(registro.ncm).lower() or
                            pesquisa.lower() in str(registro.cest).lower()]

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
        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns((0.4, 2, 1, 2, 2, 1, 1, 1, 1))
        col1.header("ID")
        col2.header("Nome")
        col3.header("Barras")
        col4.header("Quantidade")
        col5.header("NCM")
        col6.header("CEST")
        col7.header("Grupo")
        col8.header("‎")
        col9.header("‎")
        
        if registros:
            for x, item in enumerate(registros[inicio:fim]):
                col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns((0.4, 2, 1, 2, 2, 1, 1, 1, 1))
                col1.write(str(item.id))
                col2.write(item.nome)
                col3.write(item.barras)
                col4.write(str(item.quantidade))
                col5.write(item.ncm)
                col6.write(item.cest)
                col7.write(item.grupo)


                # Botão Excluir
                button_space_excluir = col8.empty()
                button_id_excluir_financeiro = 'btnExcluir' + str(item.id)
                on_click_excluir = button_space_excluir.button('Excluir', key=button_id_excluir_financeiro)
                button_space_alterar = col9.empty()
                button_id_alterar = 'btnAlterar' + str(item.id)
                on_click_alterar = button_space_alterar.button('Alterar', key=button_id_alterar)

            if on_click_excluir:
                ProdutosController.excluir(item.id)
                button_id_excluir = 'btnExcluir'
                on_click_excluir = button_space_excluir.button('Excluído!!')
                st.experimental_rerun()
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=item.id
                )
                st.experimental_rerun()