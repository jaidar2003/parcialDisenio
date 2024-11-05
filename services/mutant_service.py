from repositories.dna_repository import DnaRepository


class MutantService:
    def __init__(self):
        self.repository = DnaRepository()

    def is_mutant(self, dna):
        n = len(dna)
        sequences_found = 0

        # Verificar filas
        for row in dna:
            if self._has_sequence(row):
                sequences_found += 1
                print(f"Secuencia encontrada en fila: {row}")
            if sequences_found > 1:
                print("Más de una secuencia encontrada en filas. Es mutante.")
                return True

        # Verificar columnas
        for col in range(n):
            column = ''.join([dna[row][col] for row in range(n)])  # Columna como string
            if self._has_sequence(column):
                sequences_found += 1
                print(f"Secuencia encontrada en columna: {column}")
            if sequences_found > 1:
                print("Más de una secuencia encontrada en columnas. Es mutante.")
                return True

        # Verificar diagonales de izquierda a derecha y de derecha a izquierda
        for i in range(n - 3):
            for j in range(n - 3):
                # Diagonal de izquierda a derecha
                if dna[i][j] == dna[i + 1][j + 1] == dna[i + 2][j + 2] == dna[i + 3][j + 3]:
                    sequences_found += 1
                    print(f"Secuencia encontrada en diagonal izquierda a derecha comenzando en ({i},{j})")
                # Diagonal de derecha a izquierda
                if dna[i][j + 3] == dna[i + 1][j + 2] == dna[i + 2][j + 1] == dna[i + 3][j]:
                    sequences_found += 1
                    print(f"Secuencia encontrada en diagonal derecha a izquierda comenzando en ({i},{j + 3})")
                if sequences_found > 1:
                    print("Más de una secuencia encontrada en diagonales. Es mutante.")
                    return True

        print("No se encontraron suficientes secuencias. No es mutante.")
        return False  # Si no se encontraron más de una secuencia, no es mutante

    def _has_sequence(self, sequence):
        """Verifica si hay una secuencia de cuatro letras iguales consecutivas en una fila o columna."""
        count = 1
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i - 1]:
                count += 1
                if count == 4:
                    return True
            else:
                count = 1
        return False

    def save_dna(self, dna, is_mutant):
        return self.repository.save_dna(dna, is_mutant)

    def get_stats(self):
        count_mutant_dna = self.repository.count_mutant_dna()
        count_human_dna = self.repository.count_human_dna()
        ratio = count_mutant_dna / count_human_dna if count_human_dna > 0 else 0
        return {
            "count_mutant_dna": count_mutant_dna,
            "count_human_dna": count_human_dna,
            "ratio": ratio
        }
