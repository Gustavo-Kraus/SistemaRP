import streamlit as st
import controllers.ProdutosController as ProdutosController
import models.Produtos as produto


def cadastrar():
        st.title('Cadastrar produto')
        with st.form(key="Estoque"):
            st.subheader('Geral')
            input_nome_produto = st.text_input(label="Nome do produto")
            input_cod_barras = st.text_input(label="Código de Barras")
            input_quantidade = st.number_input(label="Quantidade", format="%d", step=1)
            input_cod_ncm = st.text_input(label="Código NCM", placeholder='12345678')
            input_cod_cest = st.text_input(label="Código CEST")
            input_nome_grupo = st.text_input(label="Nome do grupo")
            st.subheader('Valores')
            input_preco_custo = st.text_input(label="Preço de Custo")
            input_preco_venda = st.text_input(label="Preço de Venda")
            input_button_submit = st.form_submit_button("Cadastrar")
            if input_button_submit:
                produto.id = ProdutosController.ultimomaisum()
                produto.nome = input_nome_produto
                produto.barras = input_cod_barras
                produto.quantidade = input_quantidade
                produto.ncm = input_cod_ncm
                produto.cest = input_cod_cest
                produto.grupo = input_nome_grupo
                produto.custo = input_preco_custo
                produto.venda = input_preco_venda
                ProdutosController.IncluirProdutos(produto)
                st.success("Produto incluido com sucesso!")
