import unittest
from models.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def test_atiende_dia(self):
        especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.assertTrue(especialidad.atiende_dia("lunes"))
        self.assertFalse(especialidad.atiende_dia("viernes"))

    def test_dias_atencion(self):
        especialidad = Especialidad("Neurología", ["martes", "jueves"])
        self.assertEqual(especialidad.__Especialidad__dias_atencion, ["martes", "jueves"])

if __name__ == '__main__':
    unittest.main()