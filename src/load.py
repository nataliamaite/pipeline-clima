#Salva os dados transformados no PostgreSQL
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def conectar_banco():

    conexao = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return conexao


def carregar_dados(df):

    conexao = conectar_banco()
    #ponteiro que executa comandos SQL dentro do banco de dados:
    cursor = conexao.cursor()

    for _, linha in df.iterrows():#passa por cada linha da tabela (DataFrame/Pandas)

        cursor.execute(
            """
            INSERT INTO clima (
                data_hora,
                temperatura,
                umidade,
                velocidade_vento,
                precipitacao,
                codigo_clima,
                condicao_climatica,
                cidade
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (cidade, data_hora)
            DO NOTHING
            """,
            (
                linha["data_hora"],
                linha["temperatura"],
                linha["umidade"],
                linha["velocidade_vento"],
                linha["precipitacao"],
                linha["codigo_clima"],
                linha["condicao_climatica"],
                linha["cidade"]
            )
        )

    #Salva as alterações no banco permanentemente:
    conexao.commit()

    cursor.close()
    conexao.close()

    print("Dados carregados com sucesso!")