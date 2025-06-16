import unittest
from models.clinica import Clinica
from models.paciente import Paciente
from models.medico import Medico
from models.exceptions import PacienteExistenteException

class TestClinica(unittest.TestCase):
    def test_agregar_paciente(self):
        clinica = Clinica()
        p = Paciente("Ana", "87654321", "01/01/2000")
        clinica.agregar_paciente(p)
        with self.assertRaises(PacienteExistenteException):
            clinica.agregar_paciente(p)

if __name__ == '__main__':
    unittest.main()