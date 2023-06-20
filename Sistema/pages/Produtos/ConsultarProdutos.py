import streamlit as st
import controllers.ProdutosController as ProdutosController
import models.Produtos as produto
import pandas as pd


def consultar():
    st.title('Produtos')
    produtosList = []
    for item in ProdutosController.SelecionarTodos():
        produtosList.append([item.id, item.nome, item.barras, item.quantidade, item.ncm, item.cest, item.grupo, item.custo, item.venda])
    df = pd.DataFrame(
        produtosList,
        columns=['id', 'nome', 'barras', 'quantidade', 'ncm', 'cest', 'grupo', 'custo', 'venda']
    )
    st.table(df)