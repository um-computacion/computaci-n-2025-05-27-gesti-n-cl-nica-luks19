import unittest
from datetime import datetime
from models.clinica import Clinica
from models.paciente import Paciente
from models.medico import Medico
from models.especialidad import Especialidad
from models.exceptions import (
    PacienteExistenteException,
    PacienteNoEncontrado,
    MedicoNoDisponible,
    TurnoOcupado
)

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan", "12345678", "01/01/2000")
        self.medico = Medico("Dr. Smith", "MP-12345")
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.especialidad = Especialidad("Cardiología", ["lunes"])
        self.clinica.agregar_especialidad_a_medico("MP-12345", self.especialidad)

    def test_agregar_paciente(self):
        p = Paciente("Ana", "87654321", "01/01/2000")
        self.clinica.agregar_paciente(p)
        with self.assertRaises(PacienteExistenteException):
            self.clinica.agregar_paciente(p)

    def test_agregar_medico_duplicado(self):
        m = Medico("Dr. House", "MP-12345")
        with self.assertRaises(Exception):
            self.clinica.agregar_medico(m)

    def test_agendar_turno_valido(self):
        fecha = datetime.strptime("16/06/2025 10:00", "%d/%m/%Y %H:%M")
        self.clinica.agendar_turno("12345678", "MP-12345", fecha)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)

    def test_turno_duplicado(self):
        fecha = datetime.strptime("16/06/2025 10:00", "%d/%m/%Y %H:%M")
        self.clinica.agendar_turno("12345678", "MP-12345", fecha)
        with self.assertRaises(TurnoOcupado):
            self.clinica.agendar_turno("12345678", "MP-12345", fecha)

    def test_agendar_turno_paciente_no_existe(self):
        fecha = datetime.strptime("16/06/2025 10:00", "%d/%m/%Y %H:%M")
        with self.assertRaises(PacienteNoEncontrado):
            self.clinica.agendar_turno("99999999", "MP-12345", fecha)

    def test_agendar_turno_medico_no_existe(self):
        fecha = datetime.strptime("16/06/2025 10:00", "%d/%m/%Y %H:%M")
        with self.assertRaises(MedicoNoDisponible):
            self.clinica.agendar_turno("12345678", "MP-99999", fecha)

    def test_emitir_receta_valida(self):
        self.clinica.emitir_receta("12345678", "MP-12345", ["Paracetamol"])
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.get_recetas()), 1)

    def test_emitir_receta_paciente_no_existe(self):
        with self.assertRaises(PacienteNoEncontrado):
            self.clinica.emitir_receta("99999999", "MP-12345", ["Paracetamol"])

    def test_emitir_receta_medico_no_existe(self):
        with self.assertRaises(MedicoNoDisponible):
            self.clinica.emitir_receta("12345678", "MP-99999", ["Paracetamol"])

    def test_historia_clinica_turnos_y_recetas(self):
        fecha = datetime.strptime("16/06/2025 10:00", "%d/%m/%Y %H:%M")
        self.clinica.agendar_turno("12345678", "MP-12345", fecha)
        self.clinica.emitir_receta("12345678", "MP-12345", ["Ibuprofeno"])
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.get_turnos()), 1)
        self.assertEqual(len(historia.get_recetas()), 1)

if __name__ == '__main__':
    unittest.main()