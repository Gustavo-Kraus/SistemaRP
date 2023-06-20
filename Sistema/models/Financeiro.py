class Financeiro:
    def __init__(self, id,  client_id_financeiro, valor, valor_pago, data_registro, data_validade, observacoes):
        self.id = id
        self.client_id_financeiro = client_id_financeiro
        self.valor = valor
        self.valor_pago = valor_pago
        self.data_registro = data_registro
        self.data_validade = data_validade
        self.observacoes = observacoes
