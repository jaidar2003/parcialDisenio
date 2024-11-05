from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./mutant_db.sqlite3"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    import models.dna_model
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        return db  # Devuelve directamente la sesión
    finally:
        db.close()
