# Nossa tabela
import database
from sqlalchemy import Column, Integer, String
from database import Base

# Classe que representa nossa tabela "pets" no banco de dados


class PetTable(Base):
    __tablename__ = "pets"  # Nome da nossa tabela no MYSQL

    # Nossas colunas

    # id -> Identificador único

    id = Column(
        Integer, primary_key=True, index=True
    )  # index informa ao banco de dados uma criação de um índice separado para essa coluna
    nome = Column(String(50))  # nome
    idade = Column(Integer)  # Idade
    especie = Column(String(30))  # espécie
    nome_dono = Column(String(30))  # nome do dono do pet
    raca = Column(String(30))  # raça
