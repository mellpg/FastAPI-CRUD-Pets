# Entrada de dados

from fastapi import FastAPI
from database import Base, engine
from routes import pet


# Criando a instância do app

app = FastAPI()

# Conectando as rotas
app.include_router(pet.router)


# Criando tabelas no banco caso não existam
# Esse comando é uma instrução para o SQLAlchemy (ORM DO PY)
# para criar todas as tabelas definidas em nosso modelo db que ainda não existam no db

# Base -> Nossa classe declarativa. Responsável por rastrear todos os modelos (classes)
# que herdam dela e que representam as tabelas.

# metadata -> É um objeto que contém uma coleção de informações sobre as tabelas, colunas e relacionamentos

# create_all -> Método que percorre todas as tabelas conhecidas e emite o comando CREATE TABLE (cria as ausentes)

# bind=engine -> Indica qual conexão deve ser usada
Base.metadata.create_all(bind=engine)


# Mensagem de retorno:

print("Banco de dados pronto e tabelas verificadas!")
