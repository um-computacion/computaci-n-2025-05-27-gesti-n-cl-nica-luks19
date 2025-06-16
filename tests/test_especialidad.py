import unittest
from models.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def test_atiende_dia(self):
        especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.assertTrue(especialidad.atiende_dia("lunes"))
        self.assertFalse(especialidad.atiende_dia("viernes"))

    def test_dias_atencion(self):
        especialidad = Especialidad("Neurología", ["martes", "jueves"])
        self.assertEqual(especialidad.get_dias_atencion(), ["martes", "jueves"])

    def test_str(self):
        especialidad = Especialidad("Pediatría", ["lunes", "martes"])
        self.assertEqual(str(especialidad), "Pediatría")

if __name__ == '__main__':
    unittest.main() 