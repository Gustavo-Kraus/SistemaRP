import streamlit as st
import controllers.ClienteController as ClienteController
import controllers.FinanceiroController as FinanceiroController
import models.Financeiro as Financeiro
from models.Financeiro_selecionar_todos import Financeiro


st.title('Criar Financeiro')

    # Campo de busca do cliente
pesquisa_cliente = st.text_input('Pesquisar cliente por nome, CPF, ID, etc.')

    # Filtrar a lista de clientes com base na pesquisa
clientes = ClienteController.SelecionarTodos()
if pesquisa_cliente:
        clientes = [cliente for cliente in clientes if
                    pesquisa_cliente.lower() in str(cliente.id).lower() or
                    pesquisa_cliente.lower() in str(cliente.cpf).lower() or
                    pesquisa_cliente.lower() in cliente.nome.lower() or
                    pesquisa_cliente.lower() in cliente.fantasia.lower() or
                    pesquisa_cliente.lower() in cliente.rgie.lower() or
                    pesquisa_cliente.lower() in cliente.email.lower()]

    # Selecionar o cliente
selected_cliente = st.selectbox('Selecione o cliente:', clientes, format_func=lambda cliente: cliente.nome if cliente else '')

if selected_cliente:
        # Campo de valor a pagar
        valor = st.text_input('Valor a pagar:')

        # Campo de valor pago
        valor_pago = st.text_input('Valor pago:')

        # Campo de data de registro
        data_registro = st.date_input('Data de Registro:')

        # Campo de data de validade
        data_validade = st.date_input('Data de Validade:')

        # Campo de observações
        observacoes = st.text_area('Observações:')

        # Botão para adicionar o registro financeiro
        if st.button('Adicionar Registro'):
            financeiro = Financeiro(client_id_financeiro=selected_cliente.id, valor=valor, valor_pago=valor_pago, data_registro=data_registro, data_validade=data_validade, observacoes=observacoes)
            FinanceiroController.adicionar_registro(financeiro)
            st.success('Registro financeiro adicionado com sucesso!')
        