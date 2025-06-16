from datetime import datetime
from .paciente import Paciente
from .medico import Medico
from .turno import Turno
from .historia_clinica import HistoriaClinica
from .exceptions import *

class Clinica:
    def __init__(self):
        self.__pacientes = {}  # {dni: Paciente}
        self.__medicos = {}    # {matricula: Medico}
        self.__turnos = []     # List[Turno]
        self.__historias_clinicas = {}  # {dni: HistoriaClinica}

    def agregar_paciente(self, paciente: Paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise PacienteExistenteException(f"El DNI {dni} ya está registrado")
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise MedicoExistenteException(f"La matrícula {matricula} ya existe")
        self.__medicos[matricula] = medico

    # Implementa aquí los demás métodos (agendar_turno, emitir_receta, etc.)