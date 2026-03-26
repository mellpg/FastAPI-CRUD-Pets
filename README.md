# 🐾 FastAPI-CRUD-Pets

Este projeto é uma API RESTful para o gerenciamento de um Pet Shop, permitindo o controle completo de registros de animais e seus proprietários. Desenvolvido com foco em escalabilidade e organização modular.

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.12
* **Framework:** FastAPI
* **ORM:** SQLAlchemy
* **Validação:** Pydantic
* **Banco de Dados:** MySQL (Driver PyMySQL)
* **Ambiente:** Virtualenv (venv)

## 🏗️ Arquitetura do Projeto

O projeto foi dividido em módulos para facilitar a manutenção e evolução do sistema:

* `crud/`: Funções de persistência e manipulação de dados.
* `models/`: Mapeamento das tabelas do banco de dados.
* `routes/`: Definição dos endpoints e lógica das rotas.
* `schemas/`: Modelagem e validação dos dados (entrada/saída).
* `database.py`: Configuração da engine e sessões do MySQL.

## ✨ Funcionalidades Principais

* **Cadastro:** Registro de nome, raça, idade do pet e nome do proprietário.
* **Leitura:** Consulta detalhada dos registros armazenados.
* **Edição:** Atualização de qualquer informação cadastrada.
* **Exclusão:** Remoção definitiva de registros do sistema.

## 🧠 Aprendizados Relevantes

Durante o desenvolvimento, consolidei conhecimentos em:
* **Modularização e Separação de Responsabilidades:** Organização de código limpo.
* **Ambientes Virtuais:** Gerenciamento de pacotes com `pip`.
* **Infraestrutura:** Tratamento de erros de conexão e configuração de portas de rede.
* **Padrões REST:** Implementação correta dos métodos HTTP e status codes.
* **Importações:** Gestão eficiente de bibliotecas e classes internas.
