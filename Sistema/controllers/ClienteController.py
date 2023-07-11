import services.database as db
import models.Cliente as cliente
import models.Cliente_ultimoid as teste 
import models.Cliente_Consulta as cliente_consulta

def Incluir(Cliente):
    query = """
    INSERT INTO dadosclientes (id, cfp_cnpj_cliente, nome_cliente, nome_fantasia_cliente, rg_ie_cliente, cep_cliente, uf_cliente, municipio_cliente, rua_cliente, numero_endereco_cliente, bairro_cliente, complemento_cliente, email_cliente, celular_cliente, telefone_cliente)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    values = (
        Cliente.id, Cliente.cpf, Cliente.nome, Cliente.fantasia, Cliente.rgie, Cliente.cep, Cliente.uf,
        Cliente.municipio, Cliente.rua, Cliente.numero, Cliente.bairro, Cliente.complemento, Cliente.email,
        Cliente.celular, Cliente.telefone
    )

    count = db.cursor.execute(query, values).rowcount
    db.cnxn.commit()

def Alterar(Cliente):
    query = """
    UPDATE dadosclientes SET
        id = ?,
        cfp_cnpj_cliente = ?,
        nome_cliente = ?,
        nome_fantasia_cliente = ?,
        rg_ie_cliente = ?,
        cep_cliente = ?,
        uf_cliente = ?,
        municipio_cliente = ?,
        rua_cliente = ?,
        numero_endereco_cliente = ?,
        bairro_cliente = ?,
        complemento_cliente = ?,
        email_cliente = ?,
        celular_cliente = ?,
        telefone_cliente = ?
    WHERE id = ?
    """
    values = (
        Cliente.id, Cliente.cpf, Cliente.nome, Cliente.fantasia, Cliente.rgie, Cliente.cep, Cliente.uf,
        Cliente.municipio, Cliente.rua, Cliente.numero, Cliente.bairro, Cliente.complemento, Cliente.email,
        Cliente.celular, Cliente.telefone, Cliente.id
    )

    count = db.cursor.execute(query, values).rowcount
    db.cnxn.commit()

def ObterNomeCliente(cliente_id):
    db.cursor.execute("SELECT nome_cliente FROM dadosclientes WHERE id = ?", (cliente_id,))
    result = db.cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def SelecionarById(id):
    db.cursor.execute("SELECT * FROM dadosclientes WHERE ID = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14]))
    
    return costumerList[0]

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM dadosclientes")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente_consulta.Cliente_Consulta(row[0], row[1], row[2], row[3], row[4], row[5]))
    
    return costumerList

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

def ultimomaisum():
    for item in ultimoid():
            id_agora = item.id
            id_soma = 1
            soma = id_agora + id_soma
            return soma