from database.db_connection import get_db
from models.dna_model import Dna

class DnaRepository:
    def save_dna(self, dna_sequence, is_mutant):
        db = get_db()
        dna_str = ",".join(dna_sequence)

        # Verificar si la secuencia ya existe
        existing_dna = db.query(Dna).filter_by(dna=dna_str).first()
        
        if existing_dna:
            return False  # Ya existe, no guardar duplicado
        
        # Guardar la nueva secuencia si no es duplicada
        dna = Dna(dna=dna_str, is_mutant=is_mutant)
        db.add(dna)
        db.commit()
        return True

    def count_mutant_dna(self):
        db = get_db()
        return db.query(Dna).filter_by(is_mutant=True).count()

    def count_human_dna(self):
        db = get_db()
        return db.query(Dna).filter_by(is_mutant=False).count()
