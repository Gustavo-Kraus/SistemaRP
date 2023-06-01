from typing import List
import services.database as db
import models.Fornecedores as fornecedor

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
    fornecedor.cpfcnpj, 
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
        fornecedorList.append(fornecedor.Fornecedores(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14]))

    return fornecedorList