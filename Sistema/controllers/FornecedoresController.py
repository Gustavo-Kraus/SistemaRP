from typing import List
import services.database as db
import models.Fornecedores as fornecedores
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

def Alterar(fornecedor):
    query = """
    UPDATE dadosfornecedor SET
        id = ?,
        cfp_cnpj_fornecedor = ?,
        nome = ?,
        nome_fantasia_fornecedor = ?,
        rg_ie_fornecedor = ?,
        cep_fornecedor = ?,
        uf_fornecedor = ?,
        municipio_fornecedor = ?,
        rua_fornecedor = ?,
        numero_endereco_fornecedor = ?,
        bairro_fornecedor = ?,
        complemento_fornecedor = ?,
        email_fornecedor = ?,
        celular_fornecedor = ?,
        telefone_fornecedor = ?
    WHERE id = ?
    """
    values = (
        fornecedor.id, fornecedor.cpf, fornecedor.nome, fornecedor.fantasia, fornecedor.rgie, fornecedor.cep, fornecedor.uf,
        fornecedor.municipio, fornecedor.rua, fornecedor.numero, fornecedor.bairro, fornecedor.complemento, fornecedor.email,
        fornecedor.celular, fornecedor.telefone, fornecedor.id
    )

    count = db.cursor.execute(query, values).rowcount
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

def ultimomaisum():
    for item in ultimoid():
            id_agora = item.id
            id_soma = 1
            soma = id_agora + id_soma
            return soma

def SelecionarById(id):
    db.cursor.execute("SELECT * FROM dadosfornecedor WHERE ID = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(fornecedores.Fornecedores(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14]))
    
    return costumerList[0]