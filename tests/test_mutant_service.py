import unittest
from services.mutant_service import MutantService
from unittest.mock import patch
from io import StringIO

class TestMutantService(unittest.TestCase):
    def setUp(self):
        self.mutant_service = MutantService()

    def test_is_mutant_true(self):
        dna_mutante = [
            "ATGCGA",
            "CAGTGC",
            "TTATGT",
            "AGAAGG",
            "CCCCTA",
            "TCACTG"
        ]
        self.assertTrue(self.mutant_service.is_mutant(dna_mutante))

    def test_is_mutant_false(self):
        dna_humano = [
            "ATGCGA",
            "CCGTGC",
            "TTATGT",
            "AGAACG",
            "ACACTA",
            "TCACTA"
        ]
        self.assertFalse(self.mutant_service.is_mutant(dna_humano))

    def test_is_mutant_diagonal(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            dna_mutante = [
                "ATGCGC",
                "CAGTCC",
                "TTACGC",
                "AGCACT",
                "ACACTA",
                "TCACTA"
            ]
            self.assertTrue(self.mutant_service.is_mutant(dna_mutante))
            self.assertIn("Secuencia encontrada en diagonal izquierda a derecha comenzando en (0,0)", fake_out.getvalue())
            self.assertIn("Secuencia encontrada en diagonal derecha a izquierda comenzando en (0,5)", fake_out.getvalue())

    def test_is_mutant_masDeUnaSecuencia(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            dna_mutante = [
                "AAAAGC",
                "CCGGGG",
                "TTACGC",
                "AGCACT",
                "ACACTA",
                "TCACTA"
            ]
            self.assertTrue(self.mutant_service.is_mutant(dna_mutante))
            self.assertIn("Más de una secuencia encontrada en filas. Es mutante.", fake_out.getvalue())
            


    def test_save_dna(self):
        # Prueba para el método save_dna
        dna_sequence = ["ATGCGA", "CAGTGA", "TTATGA", "AGAAGG", "CCCCTT", "TCACTG"]
        is_mutant = True
        self.assertTrue(self.mutant_service.save_dna(dna_sequence, is_mutant))


if __name__ == "__main__":
    unittest.main()
