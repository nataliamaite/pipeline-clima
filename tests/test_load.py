import pandas as pd
from src import load


def test_carregar_dados(monkeypatch):
    #Criando um DataFrame falso:
    dados = pd.DataFrame([
        {
            "data_hora": "2026-10-01 10:00:00",
            "temperatura": 25.5,
            "umidade": 70,
            "velocidade_vento": 10.5,
            "precipitacao": 0,
            "codigo_clima": 0,
            "condicao_climatica": "Céu limpo",
            "cidade": "Campina Grande"
        }
    ])

    class CursorFalso:

        def execute(self, query, valores):
            self.query = query # Guarda o comando SQL executado
            self.valores = valores # Guarda os valores que seriam salvos

        def close(self):
            pass  # Apenas simula o fechamento

    class ConexaoFalsa:

        def __init__(self):
            self.cursor_falso = CursorFalso()

        def cursor(self):
            return self.cursor_falso  # Retorna o nosso cursor falso

        def commit(self):
            self.comitou = True       # Marca que o salvamento foi acionado

        def close(self):
            pass                     # Apenas simula o fechamento

    conexao_falsa = ConexaoFalsa()

    def conectar_falso():
        return conexao_falsa

    monkeypatch.setattr(
        load,
        "conectar_banco",
        conectar_falso
    )

    load.carregar_dados(dados)

    assert conexao_falsa.cursor_falso.query is not None
    assert conexao_falsa.cursor_falso.valores[1] == 25.5