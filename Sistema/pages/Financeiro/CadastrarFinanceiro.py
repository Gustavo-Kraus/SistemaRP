import streamlit as st
import controllers.ClienteController as ClienteController
import controllers.FinanceiroController as FinanceiroController
import models.Financeiro as Financeiro

def CadastrarFinanceiro():
    idAlteração = st.experimental_get_query_params()
    st.experimental_set_query_params()
    financeiroRecuperado = None
    if idAlteração.get("id") is not None:
        idAlteração = idAlteração.get("id")[0]
        financeiroRecuperado = FinanceiroController.SelecionarById(idAlteração)
        st.experimental_set_query_params(id=[financeiroRecuperado.id])
        st.title('Editar Financeiro')
    
    pesquisa_cliente = st.text_input('Pesquisar cliente por nome, CPF, ID, etc.')
    clientes = ClienteController.SelecionarTodos()
    
    if pesquisa_cliente:
        clientes = [cliente for cliente in clientes if
                    pesquisa_cliente.lower() in str(cliente.id).lower() or
                    pesquisa_cliente.lower() in str(cliente.cpf).lower() or
                    pesquisa_cliente.lower() in cliente.nome.lower() or
                    pesquisa_cliente.lower() in cliente.fantasia.lower() or
                    pesquisa_cliente.lower() in cliente.rgie.lower() or
                    pesquisa_cliente.lower() in cliente.email.lower()]

    selected_cliente = st.selectbox('Selecione o cliente:', clientes, format_func=lambda cliente: cliente.nome if cliente else '')
       
    if selected_cliente:
        valor = st.number_input('Valor a pagar:', value=float(financeiroRecuperado.valor) if financeiroRecuperado else 0.0)
        if valor is None:
            valor = 0.0
        valor_pago = st.number_input('Valor pago:', value=float(financeiroRecuperado.valor_pago) if financeiroRecuperado else 0.0)
        if valor_pago is None:
            valor_pago = 0.0
        data_registro = st.date_input('Data de Registro:', value=financeiroRecuperado.data_registro if financeiroRecuperado else None)
        data_validade = st.date_input('Data de Validade:', value=financeiroRecuperado.data_validade if financeiroRecuperado else None)
        observacoes = st.text_area('Observações:', value=financeiroRecuperado.observacoes if financeiroRecuperado else "")

        if st.button('Atualizar Registro'):
            if financeiroRecuperado is None:
                financeiro = Financeiro(client_id_financeiro=selected_cliente.id, valor=valor, valor_pago=valor_pago, data_registro=data_registro, data_validade=data_validade, observacoes=observacoes)
                FinanceiroController.adicionar_registro(financeiro)
                st.success('Registro financeiro adicionado com sucesso!')
            else:
                st.experimental_set_query_params()
                FinanceiroController.alterar_registro(selected_cliente.id, financeiroRecuperado, valor, valor_pago, data_validade, observacoes)
                st.success('Registro financeiro atualizado com sucesso!')
