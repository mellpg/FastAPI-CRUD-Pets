# PetShop API - Sistema de gerenciamento 

## Tecnologias utilizadas:

* Linguagem python 3.14
* Criação de um ambiente virtual venv
* Framework: FastAPI
* ORM: SQLAlchemby
* Validação: pydantic
* Driver de conexão: PyMySQL

# Arquitetura do Projeto

## O projeto foi divido em módulos para facilitar mudanças e manuntenção futura:

* crud/: Funções de persistência de dados (Create, Read, Update, Delete).
* models/: Mapeamento das tabelas do banco de dados (SQLAlchemy).
* routes/: Definição dos endpoints e lógica de rotas.
* schemas/: Modelagem e validação dos dados de entrada e saída (Pydantic).
* database.py: Configuração da engine e sessões do MySQL.

# Como executar o meu projeto? 
* Clone o repositório: git clone https://github.com/mellpg/Projeto_Pets.git
* Instale as depedências: pip install fastapi uvicorn sqlalchemy pymysql
* Configure o banco de dados: CREATE DATABASE petshop_db;
* Inicie o servidor: python -m uvicorn main:app --reload
* Abra o navegador em: http://127.0.0.1:8000/docs para testar os endpoints via Swagger.


# O que eu aprendi com esse projeto?
* A importância da modularização.
* Configuração de ambiente virtual e gerenciamento de pacotes com pip.
* Tratamento de erros de conexão e portas de rede.
* Separação de responsabilidades.
* Forma correta de importações de bibliotecas e classes.
