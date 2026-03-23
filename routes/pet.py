# Nossas rotas
# Importando nossa biblioteca(fastapi)
# Nossa classe apirouter para estruturar e agrupar as rotas (Endpoints) em arquivos separados
# Para escalabilidade
# Nossa função/classe do sistema de injeção de dependência do FastAPI (seus recursos externos)
# Exemplo de função injetora -> get_deb que criamos é uma injetora
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Dependência HTTPException
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from schemas.pet import PetCreate, PetResponse

# crud_pet é um apelido alias, se fizéssemos from crud import pet as pet (corre risco de sobreescrever)
# Exemplo se o projeto escalasse e tivéssemos que criar rotas para cada módulo:
# from app.schemas import pet as pet_schema  #  validação/dict
# from app.crud import pet as crud_pet       #  banco/commit
from crud import pet as crud_pet


# Nosso criador de rotas separado do FastAPI principal
# app = FastAPI() é o servidor inteiro
# Se nosso projeto escalasse
# O main ficaria com vários get/posts(clientes), get/posts(pets), get/posts(vendas), etc

router = APIRouter()


# Ao usuário enviar um arquivo (JSON) para o endereço do nosso site (por enquanto: meu ip/localhost) via método POST
# Nosso ip e a porta 8000 atende
# A função vai ser executada
@router.post("/pets", response_model=PetResponse)
# Recebendo objeto schema, nossa sessão e a fução injetora
def criar_pet(pet: PetCreate, db: Session = Depends(get_db)):
    # crud é nossa pasta
    # pet nome do nosso arquivo pet.py
    # crud_pet é apelido que escolhemos
    # Para ficar menos confuso: Temos pet.py em schemas, models, etc.
    return crud_pet.criar_pet(db, pet)


@router.delete("/pets/{pet_id}")
def excluir_pet(pet_id: int, db: Session = Depends(get_db)):
    # O resultado aqui vai ser True ou False
    resultado = crud_pet.deletar_pet(db, pet_id)

    if resultado == False:
        # Se o CRUD avisou que é False, a API responde com erro 404
        raise HTTPException(status_code=404, detail="Pet inexistente.")

    # Se for True, ela continua e manda o sucesso
    return {"mensagem": "Pet apagado!"}


# GET -> Listar nossos pets
# formatados conforme o nosso Schema de resposta (mostrando o ID, nome, etc.).
@router.get("/pets", response_model=list[PetResponse])
# Recebendo parâmetro da nossa sessão do banco e a função injetora de conexão com o banco
def listar_pets(db: Session = Depends(get_db)):
    return crud_pet.listar_pets(db)


from schemas.pet import PetCreate, PetResponse, PetUpdate


# Rota para buscar UM pet específico (READ)
@router.get("/pets/{pet_id}", response_model=PetResponse)
def ler_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = crud_pet.get_pet(db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet não encontrado")
    return db_pet


# Rota para editar um pet (UPDATE)
@router.put("/pets/{pet_id}", response_model=PetResponse)
def atualizar_pet(pet_id: int, pet_data: PetUpdate, db: Session = Depends(get_db)):
    db_pet = crud_pet.update_pet(db, pet_id=pet_id, pet_data=pet_data)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet não encontrado")
    return db_pet
