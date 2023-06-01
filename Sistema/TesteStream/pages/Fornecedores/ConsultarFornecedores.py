import streamlit as st
import controllers.FornecedoresController as FornecedorController
import models.Fornecedores as fornecedor
import pandas as pd


def consultar():
    st.title('Fornecedores')
    fornecedoresList = []
    for item in FornecedorController.SelecionarTodos():
        fornecedoresList.append([item.id, item.cpfcnpj ,item.nome , item.fantasia, item.rgie, item.cep, item.uf, item.municipio, item.rua, item.numero, item.bairro, item.complemento, item.email, item.celular, item.telefone])
    df = pd.DataFrame(
        fornecedoresList,
        columns=['id', 'Cpf/Cnpj', 'Nome',  'Nome Fantasia', 'RG/IE', 'CEP', 'UF', 'Municipio', 'Rua', 'Numero', 'Bairro', 'Complemento', 'Email', 'Celular', 'telefone']
    )
    st.table(df)