import streamlit as st

bar = st.sidebar

escolha = bar.selectbox(
    'Escolha',
    ['Estoque', 'Clientes', 'Fornecedor']
)
st.write('Escolha')

if escolha == ('Estoque'):
    st.title('Aqui vai o estoque'),
else:
    st.write('Em desenvolvimento')