import unittest
from unittest.mock import patch
from cli import CLI
from models.clinica import Clinica
from models.paciente import Paciente
from models.medico import Medico

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cli = CLI()
        self.cli._CLI__clinica = Clinica()

    @patch('builtins.input', side_effect=['Juan', '12345678', '01/01/2000'])
    def test_agregar_paciente(self, mock_input):
        self.cli._CLI__agregar_paciente()
        pacientes = self.cli._CLI__clinica.obtener_pacientes()
        self.assertTrue(any(p.obtener_dni() == '12345678' for p in pacientes))

    @patch('builtins.input', side_effect=['Dr. Smith', 'MP-12345', 'Cardiologia'])
    def test_agregar_medico(self, mock_input):
        self.cli._CLI__agregar_medico()
        medicos = self.cli._CLI__clinica.obtener_medicos()
        self.assertTrue(any(m.obtener_matricula() == 'MP-12345' for m in medicos))

    @patch('builtins.input', side_effect=['MP-12345', 'Cardiología', 'lunes,miercoles'])
    def test_agregar_especialidad(self, mock_input):
        medico = Medico("Dr. Smith", "MP-12345")
        self.cli._CLI__clinica.agregar_medico(medico)
        self.cli._CLI__agregar_especialidad()
        medico = self.cli._CLI__clinica.obtener_medico_por_matricula('MP-12345')
        self.assertEqual(len(medico.obtener_especialidades()), 1)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['12345678'])
    def test_ver_historia_clinica(self, mock_input, mock_print):
        paciente = Paciente("Juan", "12345678", "01/01/2000")
        medico = Medico("Dr. Smith", "MP-12345")
        self.cli._CLI__clinica.agregar_paciente(paciente)
        self.cli._CLI__clinica.agregar_medico(medico)
        
        self.cli._CLI__clinica.emitir_receta("12345678", "MP-12345", ["Paracetamol"])
        self.cli._CLI__ver_historia_clinica()
        
        printed_output = "\n".join(str(call.args[0]) for call in mock_print.call_args_list)
        self.assertIn("Historia de Juan (DNI: 12345678)", printed_output)
        self.assertIn("1 recetas", printed_output)
        self.assertIn("Paracetamol", printed_output)

if __name__ == '__main__':
    unittest.main()