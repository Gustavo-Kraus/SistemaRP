from typing import List
import services.database as db
import models.Produtos as produto

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