import unittest
from models.historia_clinica import HistoriaClinica
from models.paciente import Paciente
from models.turno import Turno
from models.receta import Receta
from models.medico import Medico

class TestHistoriaClinica(unittest.TestCase):
    def test_agregar_turno(self):
        paciente = Paciente("Juan", "12345678", "01/01/2000")
        historia_clinica = HistoriaClinica(paciente)
        medico = Medico("Dr. Smith", "MP-12345")
        turno = Turno(paciente, medico, "10:00", "Consulta")
        historia_clinica.agregar_turno(turno)
        self.assertEqual(len(historia_clinica.get_turnos()), 1)

    def test_agregar_receta(self):
        paciente = Paciente("María", "23456789", "02/02/1999")
        historia_clinica = HistoriaClinica(paciente)
        medico = Medico("Dr. Johnson", "MP-67890")
        receta = Receta(paciente, medico, ["Paracetamol", "Ibuprofeno"])
        historia_clinica.agregar_receta(receta)
        self.assertEqual(len(historia_clinica.get_recetas()), 1)

    def test_str(self):
        paciente = Paciente("Pedro", "34567890", "03/03/1988")
        historia_clinica = HistoriaClinica(paciente)
        esperado = f"Historia de {paciente.obtener_nombre()} (DNI: {paciente.obtener_dni()}): 0 turnos, 0 recetas"
        self.assertEqual(str(historia_clinica), esperado)

if __name__ == '__main__':
    unittest.main() 