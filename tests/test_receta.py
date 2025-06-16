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
        # Solo comprobamos que aparecen los nombres y medicamentos en el string
        receta_str = str(receta)
        self.assertIn("María", receta_str)
        self.assertIn("Dr. Johnson", receta_str)
        self.assertIn("Aspirina", receta_str)
        self.assertIn("Dietroína", receta_str)

if __name__ == '__main__':
    unittest.main() 