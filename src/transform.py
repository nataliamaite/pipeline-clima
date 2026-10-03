#Dados em formato de tabela
import pandas as pd


def transformar_dados(dados):

    hourly = dados["hourly"]

    df = pd.DataFrame(hourly)

    df = df.rename(columns={
        "time": "data_hora",
        "temperature_2m": "temperatura",
        "relative_humidity_2m": "umidade",
        "wind_speed_10m": "velocidade_vento",
        "precipitation": "precipitacao",
        "weather_code": "codigo_clima"
    })

    df["data_hora"] = pd.to_datetime(df["data_hora"])

    df["cidade"] = dados["cidade"]

    mapa_clima = {
        0: "Céu limpo",
        1: "Principalmente limpo",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Névoa",
        48: "Névoa com depósito de gelo",
        51: "Garoa fraca",
        53: "Garoa moderada",
        55: "Garoa intensa",
        61: "Chuva fraca",
        63: "Chuva moderada",
        65: "Chuva intensa",
        71: "Neve fraca",
        73: "Neve moderada",
        75: "Neve intensa",
        80: "Pancadas de chuva fracas",
        81: "Pancadas de chuva moderadas",
        82: "Pancadas de chuva intensas",
        95: "Trovoada"
    }

    df["condicao_climatica"] = df["codigo_clima"].map(mapa_clima)

    print("Valores nulos:")
    print(df.isnull().sum())

    return df