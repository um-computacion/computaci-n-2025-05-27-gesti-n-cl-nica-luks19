import unittest
from models.paciente import Paciente, DNIInvalidoException

class TestPaciente(unittest.TestCase):
    def test_paciente_valido(self):
        paciente = Paciente("Juan", "12345678", "01/01/2000")
        self.assertEqual(paciente.obtener_nombre(), "Juan")
        self.assertEqual(paciente.obtener_dni(), "12345678")

    def test_dni_invalido(self):
        with self.assertRaises(DNIInvalidoException):
            Paciente("María", "1234567", "02/02/1999")

    def test_str(self):
        paciente = Paciente("Pedro", "34567890", "03/03/1988")
        self.assertEqual(str(paciente), f"Paciente: Pedro (DNI: 34567890)")

if __name__ == '__main__':
    unittest.main()