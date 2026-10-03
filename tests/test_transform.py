from src.transform import transformar_dados


def test_transformar_dados():
    #Dados fictícios para teste:
    dados = {
        "cidade": "Campina Grande",
        "hourly": {
            "time": [
                "2026-10-01T10:00",
                "2026-10-01T11:00"
            ],
            "temperature_2m": [
                25.5,
                26.0
            ],
            "relative_humidity_2m": [
                70,
                68
            ],
            "wind_speed_10m": [
                10.5,
                12.0
            ],
            "precipitation": [
                0,
                1.2
            ],
            "weather_code": [
                0,
                61
            ]
        }
    }

    df = transformar_dados(dados)

    assert len(df) == 2
    assert "data_hora" in df.columns
    assert "temperatura" in df.columns
    assert "umidade" in df.columns
    assert "cidade" in df.columns
    assert "condicao_climatica" in df.columns

    assert df["cidade"].iloc[0] == "Campina Grande"
    assert df["temperatura"].iloc[0] == 25.5