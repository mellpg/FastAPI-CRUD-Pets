# Biblioteca pydantic para garantia que os dados sigam um padrão
# Importando a classe base BaseModel "seu coração"
# Define a estruturação dos dados, conversão(parsing), validação e JSON Schema(Facilitar a conversão entre objetos Python e formato JSON.)
# Validação automática e segurança

from pydantic import BaseModel
from typing import Optional

# Schema de entrada (O que o usuário envia)


# Nosso modelo
class PetCreate(BaseModel):
    nome: str
    idade: int
    especie: str
    nome_dono: str
    raca: str


# Schema de saída (o que nossa API vai devolver)
# Como se fosse o "número do pedido"
# Os dados do PetCreate vão criar um id na tabela
class PetResponse(PetCreate):
    id: int  # Vai incluir o id gerado pelo banco

    class Config:
        # Conversão SQLAlchemy -> Pydantic
        # Fluxo:

        # 1) O user envia os dados via JSON, o FastAPI vai utilizar o PetCreate como garantia que nenhum dado tenha ficado não preenchido

        # 2) Os dados vão ser coletados e vai ser criado um objeto da nossa PetTable (SQLAlchemy)

        # 3) O SQLAlchemy traduz o seu objeto Python para um comando SQL (INSERT INTO pets...) e manda para o MySQL.

        # 4) O MYSQL salva o pet e gera seu id. O SQLAlchemy atualiza o objeto python com esse novo id

        # 5) O FastAPI usa o PetResponse para selecionar o objeto do banco e devolver para o usuário em formato JSON
        # com o novo id incluído

        # Configuração para o pydantic ler o objeto do SQLAlchemy
        # e procurar os dados através dos atributos (pet.nome) em vez de pet['nome']
        # Sem isso, teríamos que tranformar cada pet do banco em um dicionário antes de devolver
        # ao usuário
        from_attributes = True


class PetUpdate(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    raca: Optional[str] = None
    nome_dono: Optional[str] = None

    class Config:
        from_attributes = True
