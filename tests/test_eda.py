import unittest
from pathlib import Path
from src.eda import cargar_datos, derivar, resumen_grupo, outliers_iqr

class TestEDA(unittest.TestCase):
    def test_integridad(self):
        original = cargar_datos(Path(__file__).resolve().parents[1]/'F1/data/titanic.csv')
        df = derivar(original)
        self.assertEqual(df.shape,(891,17))
        self.assertEqual(int(df.survived.sum()),342)
        self.assertEqual(int(df.age.isna().sum()),177)
        self.assertEqual(int(df.deck.isna().sum()),688)
        self.assertEqual(int(original.duplicated().sum()),107)
        self.assertEqual(int(resumen_grupo(df,'sex').n.sum()),891)
        self.assertEqual(outliers_iqr(df.age)['n_atipicos'],11)
        self.assertEqual(outliers_iqr(df.fare)['n_atipicos'],116)

if __name__ == '__main__':
    unittest.main()
