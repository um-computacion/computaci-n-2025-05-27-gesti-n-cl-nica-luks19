import unittest
from models.receta import Receta
from models.paciente import Paciente
from models.medico import Medico

class TestReceta(unittest.TestCase):
    def test_obtener_medicamentos(self):
        paciente = Paciente("Juan", "12345678", "01/01/2000")
        medico = Medico("Dr. Smith", "MP-12345")
        receta = Receta(paciente, medico, ["Paracetamol", "Ibuprofeno"])
        self.assertEqual(receta.obtener_medicamentos(), ["Paracetamol", "Ibuprofeno"])

    def test_str(self):
        paciente = Paciente("María", "23456789", "02/02/1999")
        medico = Medico("Dr. Johnson", "MP-67890")
        receta = Receta(paciente, medico, ["Aspirina", "Dietroína"])
        self.assertEqual(str(receta), f"Receta para María por Dr. Johnson: Aspirina, Dietroína")

if __name__ == '__main__':
    unittest.main()