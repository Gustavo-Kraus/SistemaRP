import services.database as database
import models.Financeiro as Financeiro
import models.financeiro_id as financeiroid
import models.Financeiro_selecionar_todos as financeiroselecionar


def adicionar_registro(financeiro):
    query = "INSERT INTO TabelaFinanceiro (cliente_id, valor, valor_pago, data_registro, data_validade, observacoes) VALUES (?, ?, ?, ?, ?, ?)"
    params = (financeiro.client_id_financeiro, financeiro.valor, financeiro.valor_pago, financeiro.data_registro, financeiro.data_validade, financeiro.observacoes)
    
    count = database.cursor.execute(query, params).rowcount
    database.cnxn.commit()

def alterar_registro(cliente_id, financeiroRecuperado, novo_valor, novo_valor_pago, nova_data_validade, novas_observacoes):
    query = "UPDATE TabelaFinanceiro SET cliente_id = ?, valor = ?, valor_pago = ?, data_validade = ?, observacoes = ? WHERE id = ?"
    params = (cliente_id, novo_valor, novo_valor_pago, nova_data_validade, novas_observacoes, financeiroRecuperado.id)

    count = database.cursor.execute(query, params).rowcount
    database.cnxn.commit()



def SelecionarTodos():
    database.cursor.execute("SELECT * FROM TabelaFinanceiro")
    financeiroList = []

    for row in database.cursor.fetchall():
        financeiro = Financeiro.Financeiro(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        financeiroList.append(financeiro)
    
    return financeiroList


def excluir_registro(id_registro):
    query = "DELETE FROM TabelaFinanceiro WHERE id = ?"
    params = (id_registro)
    
    count = database.cursor.execute(query, params).rowcount
    database.cnxn.commit()

def SelecionarById(id):
    database.cursor.execute("SELECT * FROM TabelaFinanceiro WHERE ID = ?", id)
    costumerList = []

    for row in database.cursor.fetchall():
        costumerList.append(Financeiro.Financeiro(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    
    return costumerList[0]



def ultimoid():
    database.cursor.execute("SELECT MAX(id) FROM TabelaFinanceiro ")
    testeList = []
    for row in database.cursor.fetchall():
        testeList.append(financeiroid.Financeiro(row[0]))
    return testeList

def ultimomaisum():
    for item in ultimoid():
            id_agora = item.id
            id_soma = 1
            soma = id_agora + id_soma
            return soma