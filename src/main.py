from extract import extrair_dados
from transform import transformar_dados
from load import carregar_dados
import pandas as pd


cidades = [
    {
        "nome": "Campina Grande",
        "latitude": -7.23056,
        "longitude": -35.88111
    },
    {
        "nome": "João Pessoa",
        "latitude": -7.1195,
        "longitude": -34.8450
    },
    {
        "nome": "Recife",
        "latitude": -8.0476,
        "longitude": -34.8770
    }
]


dados_transformados = []


for cidade in cidades:

    dados = extrair_dados(
        cidade["nome"],
        cidade["latitude"],
        cidade["longitude"]
    )

    df = transformar_dados(dados)

    dados_transformados.append(df)


df_final = pd.concat(
    dados_transformados,
    ignore_index=True
)


carregar_dados(df_final)

print(df_final)