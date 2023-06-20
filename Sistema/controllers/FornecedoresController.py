from typing import List
import services.database as db
import models.Fornecedores as fornecedor
import models.Fornecedor_Consulta as fornecedor_consulta
import models.Fornecedor_id as fornecedor
import services.database as db


def IncluirFornecedores (fornecedor):
    count = db.cursor.execute("""
    INSERT INTO dadosfornecedor (
    id, 
    cfp_cnpj_fornecedor, 
    nome, 
    nome_fantasia_fornecedor, 
    rg_ie_fornecedor, 
    cep_fornecedor, 
    uf_fornecedor, 
    municipio_fornecedor, 
    rua_fornecedor, 
    numero_endereco_fornecedor, 
    bairro_fornecedor, 
    complemento_fornecedor, 
    email_fornecedor, 
    celular_fornecedor, 
    telefone_fornecedor)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
    fornecedor.id, 
    fornecedor.cpf, 
    fornecedor.nome, 
    fornecedor.fantasia, 
    fornecedor.rgie, 
    fornecedor.cep, 
    fornecedor.uf, 
    fornecedor.municipio, 
    fornecedor.rua, 
    fornecedor.numero, 
    fornecedor.bairro, 
    fornecedor.complemento, 
    fornecedor.email, 
    fornecedor.celular, 
    fornecedor.telefone).rowcount
    db.cnxn.commit()


def SelecionarTodos():
    db.cursor.execute("SELECT * FROM dadosfornecedor")
    fornecedorList = []

    for row in db.cursor.fetchall():
        fornecedorList.append(fornecedor_consulta.Fornecedores_Consulta(row[0], row[1], row[2], row[3], row[4], row[5]))

    return fornecedorList

def excluir(id):
    count = db.cursor.execute("""
    DELETE FROM dadosfornecedor WHERE id = ?""",
    id).rowcount
    db.cnxn.commit()

def ultimoid():
    db.cursor.execute("SELECT MAX(id) FROM dadosfornecedor ")
    testeList = []
    for row in db.cursor.fetchall():
        testeList.append(fornecedor.Fornecedor(row[0]))
    return testeList

