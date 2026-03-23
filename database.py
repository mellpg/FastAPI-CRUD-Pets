# Responsabilidade do SQLAlchemy

# SQLAClchemy é um framework de mapeamento objeto-relacional SQL (ORM) de
# Código aberto

# ORM -> ma técnica de programação que auxilia na conversão de dados entre DB relacionais
# e linguagens de programação que são orientadas à objetos.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Nossa URL de conexão com o MYSQL
# mysql + pymysql -> Driver

# Criando banco
DATABASE_URL = "mysql+pymysql://root:mel160606@localhost:3306/petshop_db"

# Responsável pela comunicação com o nosso banco
engine = create_engine(DATABASE_URL)

# Sessionlocal -> Nossa "Fábrica" de sessões, cada request usa uma sessão
SessionLocal = sessionmaker(
    # Para cada sessão é necessário chamar session.commit()
    # Sem esses ao fazer alterações, seria impossível desfazer
    # usando session.rollback()
    autocommit=False,  # Não vai salvar
    autoflush=False,  # Evita sync automático com o banco
    bind=engine,  # conecta ao engine
)

# Base = nossa classe para criar as tabelas (ORM)

Base = declarative_base()

# Dependência do  FastAPI para abrir e fechar conexão automaticamente


# Nossa função injetora (para realizar a conexão com o MYSQL)
def get_db():
    db = SessionLocal()
    try:
        yield db  # Entregando nossa sessão para a rota
    finally:
        db.close()  # Fecha a sessão depois da request
