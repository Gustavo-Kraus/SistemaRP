import streamlit as st
from pages.Cliente import CadastrarCliente, ConsultarCliente
from pages.Financeiro import CadastrarFinanceiro, ConsultarFinanceiro
from pages.Fornecedores import CadastrarFornecedores, ConsultarFornecedores
from pages.Produtos import ConsultarProdutos, CadastrarProdutos


# Dicionário de usuários e permissões permitidas
usuarios_permitidos = {
    "gu": {
        "senha": "123",
        "permissoes": ["bar1", "bar2"]
    },
    "gu2": {
        "senha": "123",
        "permissoes": ["bar1"]
    }
}

st.set_page_config(layout="wide")

# Função auxiliar para atualizar a sessão
def update_session_state(**kwargs):
    for key, value in kwargs.items():
        setattr(st.session_state, key, value)

# Página de login
def login():
    st.title("Login")

    with st.form(key="login_form"):
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")

        login_message = st.empty()  # Espaço para exibir mensagem de erro/sucesso

        submit_button = st.form_submit_button("Entrar")

        if submit_button:
            if username in usuarios_permitidos and usuarios_permitidos[username]["senha"] == password:
                update_session_state(logged_in=True, username=username)
            else:
                login_message.error("Usuário ou senha inválidos")

# Página inicial
def home():
    st.title("Olá, " + st.session_state.username)

st.sidebar.title("Menu")

if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    login()
else:
    # Exibir botão de logout na barra lateral
    if st.sidebar.button("Logout"):
        update_session_state(logged_in=False, username=None)
        st.experimental_rerun()

    home()

    # Exibir conteúdo da barra lateral quando logado
    bar1_allowed = False
    bar2_allowed = False

    if st.session_state.username in usuarios_permitidos:
        user_permissions = usuarios_permitidos[st.session_state.username]["permissoes"]
        if "bar1" in user_permissions:
            bar1_allowed = True
        if "bar2" in user_permissions:
            bar2_allowed = True

    bar = st.sidebar.selectbox('Cadastro', ['', 'Clientes','Adicionar Cliente', 'Produtos', 'Adicionar Produtos' ,'Fornecedores', 'Adicionar Fornecedor' ] if bar1_allowed else [''])
    bar2 = st.sidebar.selectbox('Financeiro', ['', 'Financeiro', 'Cadastrar Financeiro'] if bar2_allowed else [''])

    mostrar_cadastrar_cliente = False

    if bar == 'Cadastrar Cliente':
        st.experimental_set_query_params()
        mostrar_cadastrar_cliente = True

    if mostrar_cadastrar_cliente:
        CadastrarCliente.cadastrar()

    if bar == 'Clientes':
        ConsultarCliente.ConsultarCliente()
    
    if bar == 'Adicionar Cliente':
        CadastrarCliente.cadastrar()

    if bar == 'Adicionar Produtos':
        CadastrarProdutos.cadastrar()

    if bar == 'Produtos':
        ConsultarProdutos.consultar()

    if bar == 'Fornecedores':
        ConsultarFornecedores.Consultar()

    if bar == 'Adicionar Fornecedor':
        CadastrarFornecedores.cadastrar()

    if bar2 == 'Cadastrar Financeiro':
        st.experimental_set_query_params()
        CadastrarFinanceiro.CadastrarFinanceiro()

    if bar2 == 'Financeiro':
        ConsultarFinanceiro.ConsultarFinanceiro()


    # Espaço em branco no lugar da barra lateral quando não logado
    st.sidebar.empty()
