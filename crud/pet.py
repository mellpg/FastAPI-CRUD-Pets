# Nosso CRUD (CRIAR, READ, UPDATE, DELETE)

from sqlalchemy.orm import Session
from models.pet import PetTable
from schemas.pet import PetCreate
from schemas.pet import PetCreate, PetUpdate


# Função para o INSERT no banco


def criar_pet(db: Session, pet: PetCreate):

    # Transformando Schema em objeto do banco

    novo_pet = PetTable(**pet.dict())

    # Adicionando na sessão (ainda não salva)

    db.add(novo_pet)

    # Salvando no banco

    db.commit()

    # Atualiza objeto com ID gerado

    db.refresh(novo_pet)

    return novo_pet


# READ (Buscar um único Pet)
def get_pet(db: Session, pet_id: int):
    return db.query(PetTable).filter(PetTable.id == pet_id).first()


# UPDATE (Atualizar um Pet)
def update_pet(db: Session, pet_id: int, pet_data: PetUpdate):
    db_pet = db.query(PetTable).filter(PetTable.id == pet_id).first()
    if db_pet:
        update_data = pet_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_pet, key, value)
        db.commit()
        db.refresh(db_pet)
    return db_pet


def deletar_pet(db: Session, pet_id: int):
    # 1. Busca o pet pelo ID
    db_pet = db.query(PetTable).filter(PetTable.id == pet_id).first()

    if db_pet:
        db.delete(db_pet)  # Marca para deletar
        db.commit()  # Confirma no banco
        return True

    # Vai retornar falso caso o id não exista
    # Vai pular todo o bloco de delete e commit
    return False


# Função responsável pelo SELECT *
# Recebe como parãmetro a sessão do banco de dados
# listar dados


def listar_pets(db: Session):
    # Usando biblioteca SQLAlchemy
    # Inicia consulta da tabela mapeada PetTable
    return db.query(PetTable).all()  # Retornando todos os registros

    # Tranforma o Schema(o que definimos que o usuário entre) em objeto do banco
    # O nosso objeto pet é uma instância (objeto específico criado a partir de uma classe) do pydantic
    # o dict abre coleta os dados e os tranforma em um dicionário comum
    # instância pydantic (PetCreate) -> É a validação. Garantia que que os dados estão corretos
    # instância SQLAlchemy (PetTable) -> É um objeto do banco de dados. Traduz comandos SQL
    # Fazer novo_pet = PetTable(pet) iria dar um erro:
    # o dict tranforma a estrutura do pydantic em um dicionário comum
    # O SQL só aceita textos e números
    # Pydantic:
    # Modelo Pydantic
    #   class Usuario(BaseModel):
    #             id: int
    #             nome: str
    #            email: EmailStr  # Valida se é um e-mail válido

    # Com validação: se o 'id' não for inteiro, lança erro.
    # se o 'email' estiver errado, lança erro.
    # user = Usuario(id=1, nome="João", email="joao@exemplo.com")
    #  novo_pet = PetTable(**pet.dict())

    # Dicionário comum:

    # usuario = {
    #     "id": 1,
    #     "nome": "João",
    #     "email": "joao@exemplo.com"
    # }
    # Sem validação: posso alterar o id para string sem erros
    #  usuario["id"] = "ABC"
