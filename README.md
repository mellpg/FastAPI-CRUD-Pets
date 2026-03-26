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

# O que eu aprendi com esse projeto?
* A importância da modularização.
* Configuração de ambiente virtual e gerenciamento de pacotes com pip.
* Tratamento de erros de conexão e portas de rede.
* Separação de responsabilidades.
* Forma correta de importações de bibliotecas e classes.
* API REST.

# Sobre o projeto 
## Funcionalidades principais:
* Cadastro: Inserção de nome, raça, idade do pet e nome do dono.
* Leitura: Visualização detalhada dos registros armazenados.
* Edição: Atualização de qualquer informação previamente cadastrada.
* Exclusão: Remoção definitiva de registros do sistema.
