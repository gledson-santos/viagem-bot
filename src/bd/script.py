from src.bd.conect_bd import ConectBd
from datetime import datetime


class Script(object):

    def __init__(self):
        self.conexao = ConectBd()

    def consulta_parametros(self):
        sql = 'select * from parametros'
        return self.conexao.busca(sql)

    def atualiza_valor_voos(self, valor):
        sql = 'update parametros set valor={} where tipo_parametro="valor_voo";'.format(valor)
        return self.conexao.executa(sql)

    def consulta_menor_valor_passagem(self):
        data = datetime.now().strftime("%d-%m-%y")
        sql = 'SELECT MIN(valor) AS valor FROM voos WHERE data_consulta >= {}'.format(data)
        return self.conexao.busca(sql)

    def consulta_data_ultima_verificacao(self):
        sql = 'SELECT id, data_consulta FROM voos ORDER BY 1 DESC LIMIT 1;'
        return self.conexao.busca(sql)

    def consulta_paramentros(self):
        sql = 'SELECT * FROM parametros;'
        return self.conexao.busca(sql)
