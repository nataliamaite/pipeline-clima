#Busca os dados da API para cada cidade.
import requests

#agora a função precisa de extrair_dados("Campina Grande", -7.23056, -35.88111)
def extrair_dados(cidade, latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation,weather_code",
        "timezone": "America/Sao_Paulo"
    }

#Execução e tratamento da resposta:

    #Envia a requisição GET para a API com os parâmetros configurados:
    resposta = requests.get(url, params=params)
    #Exibe o nome dad cidade e status HTTP da requisição:
    print(f"{cidade} - Status:", resposta.status_code)
    #Converte a resposta da requisição em dicionário:
    dados = resposta.json()
    #Nova chave para guardar o nome da cidade:
    dados["cidade"] = cidade
    #Retorna o dicionário completo:
    return dados