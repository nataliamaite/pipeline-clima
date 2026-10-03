# 🌦️ Pipeline de Dados Climáticos

Projeto de pipeline de dados desenvolvido para praticar conceitos de Engenharia de Dados utilizando Python, API, ETL, PostgreSQL e testes automatizados.

## 📌 Sobre o projeto

O pipeline coleta dados climáticos da API Open-Meteo, transforma os dados utilizando Python e Pandas e realiza a carga em um banco PostgreSQL.

O projeto também possui testes automatizados utilizando pytest.

## 🏗️ Arquitetura

```text
API Open-Meteo
      ↓
   Extract
      ↓
   Transform
      ↓
     Load
      ↓
 PostgreSQL
🛠️ Tecnologias
Python
Requests
Pandas
PostgreSQL
Pytest
Git
GitHub
GitHub Actions
📂 Estrutura do projeto
projeto-pipeline-clima/
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
🔄 Etapas do pipeline
1. Extração

Os dados são obtidos através da API Open-Meteo utilizando a biblioteca requests.

2. Transformação

Os dados recebidos são transformados utilizando Pandas:

Conversão para DataFrame
Renomeação das colunas
Conversão de datas
Inclusão da cidade
Tratamento dos códigos climáticos
3. Carga

Os dados transformados são carregados em uma tabela PostgreSQL.

O pipeline utiliza uma restrição de unicidade baseada em cidade e data/hora para evitar registros duplicados.

4. Testes

O projeto possui testes automatizados utilizando pytest.

Os testes verificam as etapas de:

Extração
Transformação
Carga
▶️ Como executar

Clone o repositório:

git clone <URL_DO_REPOSITORIO>
cd projeto-pipeline-clima

Crie um ambiente virtual:

python3 -m venv .venv

Ative o ambiente:

source .venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

Configure as variáveis de ambiente no arquivo .env:

DB_HOST=localhost
DB_PORT=5433
DB_NAME=etl_clima
DB_USER=postgres
DB_PASSWORD=sua_senha

Execute os testes:

pytest

Execute o pipeline:

python src/main.py
