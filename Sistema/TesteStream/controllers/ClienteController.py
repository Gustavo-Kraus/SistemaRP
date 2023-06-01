from typing import List
import services.database as db
import models.Cliente as cliente
import models.Cliente_teste as teste 

def Incluir (Cliente):
    count = db.cursor.execute("""
    INSERT INTO dadosclientes (id, cfp_cnpj_cliente, nome_cliente, nome_fantasia_cliente, rg_ie_cliente, email_cliente)
    VALUES (?,?,?,?,?,?)""",
    Cliente.id, Cliente.cpf, Cliente.nome, Cliente.fantasia, Cliente.rgie, Cliente.email).rowcount
    db.cnxn.commit()


def excluir(id):
    count = db.cursor.execute("""
    DELETE FROM dadosclientes WHERE id = ?""",
    id).rowcount
    db.cnxn.commit()

def ultimoid():
    db.cursor.execute("SELECT MAX(id) FROM dadosclientes ")
    testeList = []
    for row in db.cursor.fetchall():
        testeList.append(teste.Cliente(row[0]))
    return testeList




def SelecionarTodos():
    db.cursor.execute("SELECT * FROM dadosclientes")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3], row[4], row[5]))
    
    return costumerList