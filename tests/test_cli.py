import unittest
from unittest.mock import patch, MagicMock
from models.clinica import Clinica
from models.paciente import Paciente
from models.medico import Medico
from models.especialidad import Especialidad
from datetime import datetime

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.cli = CLI()

    @patch('builtins.input', side_effect=['Juan', '12345678', '01/01/2000'])
    def test_agregar_paciente(self, mock_input):
        self.cli.__agregar_paciente()
        self.assertIn('12345678', self.clinica.__pacientes)

    @patch('builtins.input', side_effect=['Dr. Smith', 'MP-12345'])
    def test_agregar_medico(self, mock_input):
        self.cli.__agregar_medico()
        self.assertIn('MP-12345', self.clinica.__medicos)

    @patch('builtins.input', side_effect=['MP-12345', 'Cardiología', 'lunes,miercoles'])
    def test_agregar_especialidad(self, mock_input):
        medico = Medico("Dr. Smith", "MP-12345")
        self.clinica.agregar_medico(medico)
        self.cli.__agregar_especialidad()
        self.assertEqual(len(self.clinica.__medicos['MP-12345'].__especialidades), 1)

    @patch('builtins.input', side_effect=['12345678', 'MP-12345', '18/06/2025 10:00'])
    def test_agendar_turno(self, mock_input):
        paciente = Paciente("Juan", "12345678", "01/01/2000")
        medico = Medico("Dr. Smith", "MP-12345")
        self.clinica.agregar_paciente(paciente)
        self.clinica.agregar_medico(medico)
        self.cli.__agendar_turno()
        self.assertEqual(len(self.clinica.__turnos), 1)

    @patch('builtins.input', side_effect=['12345678', 'MP-12345', 'Paracetamol,Ibuprofeno'])
    def test_emitir_receta(self, mock_input):
        paciente = Paciente("Juan", "12345678", "01/01/2000")
        medico = Medico("Dr. Smith", "MP-12345")
        self.clinica.agregar_paciente(paciente)
        self.clinica.agregar_medico(medico)
        self.cli.__emitir_receta()
        self.assertEqual(len(self.clinica.__historias_clinicas['12345678'].__recetas), 1)

    @patch('builtins.input', side_effect=['12345678'])
    def test_ver_historia_clinica(self, mock_input):
        paciente = Paciente("Juan", "12345678", "01/01/2000")
        medico = Medico("Dr. Smith", "MP-12345")
        self.clinica.agregar_paciente(paciente)
        self.clinica.agregar_medico(medico)
        self.clinica.emitir_receta("12345678", "MP-12345", ["Paracetamol", "Ibuprofeno"])
        self.cli.__ver_historia_clinica()
        # Verificar que se imprime la receta correctamente

if __name__ == '__main__':
    unittest.main()