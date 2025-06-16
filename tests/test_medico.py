import unittest
from models.medico import Medico
from models.exceptions import MatriculaInvalidaException

class TestMedico(unittest.TestCase):
    def test_creacion_valida(self):
        m = Medico("Dra. Pérez", "MP-54321")
        self.assertEqual(m.obtener_matricula(), "MP-54321")

    def test_matricula_invalida(self):
        with self.assertRaises(MatriculaInvalidaException):
            Medico("Dr. Error", "INVALID-123")

if __name__ == '__main__':
    unittest.main()