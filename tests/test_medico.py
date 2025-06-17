import unittest
from models.medico import Medico
from models.exceptions import MatriculaInvalidaException

class TestMedico(unittest.TestCase):
    def test_creacion_valida(self):
        m = Medico("Dra. Pérez", "MP-54321", ["Cardiología"])
        self.assertEqual(m.obtener_matricula(), "MP-54321")
        self.assertEqual(m.obtener_especialidades(), ["Cardiología"])

    def test_matricula_invalida(self):
        with self.assertRaises(MatriculaInvalidaException):
            Medico("Dr. Error", "INVALID-123", ["Clínica"])

    def test_str(self):
        m = Medico("Dra. Pérez", "MP-54321", ["Cardiología", "Clínica"])
        s = str(m)
        self.assertIn("Dra. Pérez", s)
        self.assertIn("MP-54321", s)
        self.assertIn("Cardiología", s)
        self.assertIn("Clínica", s)

if __name__ == '__main__':
    unittest.main()