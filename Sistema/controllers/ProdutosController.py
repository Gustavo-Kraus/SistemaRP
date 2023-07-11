from typing import List
import services.database as db
import models.Produtos as produto
import models.Produtos_ultimoid as teste

def IncluirProdutos (Produto):
    count = db.cursor.execute("""
    INSERT INTO dadosprodutos (id, nome_produto, cod_barras, quantidade, cod_ncm, cod_cest, nome_grupo, preco_custo, preco_venda)
    VALUES (?,?,?,?,?,?,?,?,?)""",
    Produto.id, Produto.nome, Produto.barras, Produto.quantidade, Produto.ncm, Produto.cest, Produto.grupo, Produto.custo, Produto.venda).rowcount
    db.cnxn.commit()


def SelecionarTodos():
    db.cursor.execute("SELECT * FROM dadosprodutos")
    produtosList = []

    for row in db.cursor.fetchall():
        produtosList.append(produto.Produtos(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    
    return produtosList

def ultimoid():
    db.cursor.execute("SELECT MAX(id) FROM dadosprodutos ")
    testeList = []
    for row in db.cursor.fetchall():
        testeList.append(teste.Produtos(row[0]))
    return testeList

def ultimomaisum():
    for item in ultimoid():
            id_agora = item.id
            id_soma = 1
            soma = id_agora + id_soma
            return soma
    
def excluir(id):
    count = db.cursor.execute("""
    DELETE FROM dadosprodutos WHERE id = ?""",
    id).rowcount
    db.cnxn.commit()