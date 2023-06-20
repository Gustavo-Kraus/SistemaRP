from typing import List
import services.database as db
import models.Cliente_Pesquisa as Pesquisa
import models.Cliente_Consulta as cliente_consulta


def consultar(nome):
    db.cursor.execute("SELECT * FROM dadosclientes WHERE nome_cliente LIKE '?%' ", nome)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente_consulta.Cliente_Consulta(row[0], row[1], row[2], row[3], row[4], row[5]))
    
    return costumerList