import unittest
from models.receta import Receta
from models.paciente import Paciente
from models.medico import Medico

class TestReceta(unittest.TestCase):
    def test_str(self):
        paciente = Paciente("María", "23456789", "02/02/1999")
        medico = Medico("Dr. Johnson", "MP-67890", ["Clínica"])
        receta = Receta(paciente, medico, ["Aspirina", "Dietroína"])
        # Solo comprobamos que aparecen los nombres y medicamentos en el string
        receta_str = str(receta)
        self.assertIn("María", receta_str)
        self.assertIn("Dr. Johnson", receta_str)
        self.assertIn("Aspirina", receta_str)
        self.assertIn("Dietroína", receta_str)

if __name__ == '__main__':
    unittest.main()