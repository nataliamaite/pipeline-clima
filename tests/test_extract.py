from src.extract import extrair_dados


def test_extrair_dados(monkeypatch):

    class RespostaFalsa:

        status_code = 200
        #Dados fictícios da resposta da API:
        def json(self):
            return {
                "hourly": {
                    "time": ["2026-10-01T10:00"],
                    "temperature_2m": [25.5],
                    "relative_humidity_2m": [70],
                    "wind_speed_10m": [10],
                    "precipitation": [0],
                    "weather_code": [0]
                }
            }

    def get_falso(url, params):
        return RespostaFalsa()

    monkeypatch.setattr(
        "src.extract.requests.get",
        get_falso
    )

    dados = extrair_dados(
        "Campina Grande",
        -7.23056,
        -35.88111
    )

    assert dados["cidade"] == "Campina Grande"
    assert "hourly" in dados
    assert "temperature_2m" in dados["hourly"]