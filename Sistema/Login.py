import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path


# --- USER AUTHENTICATION ---
nomes = ["TesteLogin"]
usernames = ["teste"]
passwords = ["teste"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_password = pickle.load(file)

authentication = stauth.Authenticate(nomes, usernames, hashed_password,
    "Main", cookie_expiry_days=0)

nome, authentication_status, username = authentication.login("Login", "Main")

if authentication_status == False:
    st.error("Nome ou senha está incorreto")

if authentication_status == nome:
    st.warning("Por favor preencha os campos!")

st.title('*Olá, seja muito bem vindo*')
st.write('Coloque sua credenciais')



#Email = st.text_input('Email', max_chars=30, placeholder='Coloque seu email',)
#Senha = st.text_input('Senha', type='password', max_chars=12, placeholder='Máximo 12 caracteres')

#st.button('Acessar')


