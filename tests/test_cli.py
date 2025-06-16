import unittest
from unittest.mock import patch
from cli.cli import CLI
from models.clinica import Clinica
from models.paciente import Paciente
from models.medico import Medico

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cli = CLI()
        self.cli._CLI__clinica = Clinica()  # Accedemos al atributo privado para testing

    @patch('builtins.input', side_effect=['Juan', '12345678', '01/01/2000'])
    def test_agregar_paciente(self, mock_input):
        self.cli._CLI__agregar_paciente()
        pacientes = self.cli._CLI__clinica.obtener_pacientes()
        self.assertTrue(any(p.obtener_dni() == '12345678' for p in pacientes))

    @patch('builtins.input', side_effect=['Dr. Smith', 'MP-12345'])
    def test_agregar_medico(self, mock_input):
        self.cli._CLI__agregar_medico()
        medicos = self.cli._CLI__clinica.obtener_medicos()
        self.assertTrue(any(m.obtener_matricula() == 'MP-12345' for m in medicos))

    @patch('builtins.input', side_effect=['MP-12345', 'Cardiología', 'lunes,miercoles'])
    def test_agregar_especialidad(self, mock_input):
        # Primero agregamos un médico
        medico = Medico("Dr. Smith", "MP-12345")
        self.cli._CLI__clinica.agregar_medico(medico)
        self.cli._CLI__agregar_especialidad()
        # Verificamos que se agregó la especialidad
        medico = self.cli._CLI__clinica.obtener_medico_por_matricula('MP-12345')
        self.assertEqual(len(medico.obtener_especialidades()), 1)

    @patch('builtins.print')  # Para capturar la salida
    @patch('builtins.input', side_effect=['12345678'])
    def test_ver_historia_clinica(self, mock_input, mock_print):
        # Configuramos datos de prueba
        paciente = Paciente("Juan", "12345678", "01/01/2000")
        medico = Medico("Dr. Smith", "MP-12345")
        self.cli._CLI__clinica.agregar_paciente(paciente)
        self.cli._CLI__clinica.agregar_medico(medico)
        self.cli._CLI__clinica.emitir_receta("12345678", "MP-12345", ["Paracetamol"])
        
        self.cli._CLI__ver_historia_clinica()
        
        # Verificamos que se imprimió algo relacionado con la receta
        self.assertTrue(
            any("Receta emitida el" in str(call.args[0]) for call in mock_print.call_args_list)
        )

if __name__ == '__main__':
    unittest.main() 