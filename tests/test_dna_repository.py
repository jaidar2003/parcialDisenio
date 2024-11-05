import unittest
from repositories.dna_repository import DnaRepository
from database.db_connection import get_db
from models.dna_model import Dna

class TestDnaRepository(unittest.TestCase):
    def setUp(self):
        self.repo = DnaRepository()
        self.db = get_db()
        
        # Eliminar todos los datos antes de insertar nuevos registros
        self.db.query(Dna).delete()
        self.db.commit()

        # Insertar datos de prueba
        self.db.add(Dna(dna="ATGCGA,CAGTGC,TTATGT,AGAAGG,CCCCTA,TCACTG", is_mutant=True))
        self.db.add(Dna(dna="GCTGTA,CAGTGC,TTGTAT,AGAGTG,CCTTTA,TCACTG", is_mutant=False))
        self.db.add(Dna(dna="TTTTTT,GGGGGG,CCCCCC,AAAAAA,TTTTTT,GGGGGG", is_mutant=True))
        self.db.commit()

    def tearDown(self):
        # Limpiar los datos de prueba
        self.db.query(Dna).delete()
        self.db.commit()
        # Cerrar la sesión
        self.db.close()

    def test_count_mutant_dna(self):
        count_mutant = self.repo.count_mutant_dna()
        self.assertEqual(count_mutant, 2)  # Esperamos 2 secuencias mutantes

    def test_count_human_dna(self):
        count_human = self.repo.count_human_dna()
        self.assertEqual(count_human, 1)  # Esperamos 1 secuencia humana

if __name__ == "__main__":
    unittest.main()
