from datetime import datetime
from .paciente import Paciente
from .medico import Medico
from .turno import Turno
from .historia_clinica import HistoriaClinica
from .receta import Receta
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

    def agregar_especialidad_a_medico(self, matricula: str, especialidad: Especialidad):
        if matricula not in self.__medicos:
            raise ValueError("Médico no registrado")
        self.__medicos[matricula].agregar_especialidad(especialidad)

    def agendar_turno(self, dni_paciente: str, matricula_medico: str, fecha_hora: datetime):
        # Validar existencia
        if dni_paciente not in self.__pacientes:
            raise ValueError("Paciente no registrado")
        if matricula_medico not in self.__medicos:
            raise ValueError("Médico no registrado")

        # Validar disponibilidad
        medico = self.__medicos[matricula_medico]
        dia_semana = fecha_hora.strftime("%A").lower()  # Ej: "monday" → "lunes"
        
        if not any(esp.atiende_dia(dia_semana) for esp in medico.obtener_especialidades()):
            raise ValueError("Médico no atiende ese día")

        # Crear y registrar turno
        paciente = self.__pacientes[dni_paciente]
        especialidad = "Consulta general"  # Puedes modificarlo según sea necesario
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)

    def emitir_receta(self, dni_paciente: str, matricula_medico: str, medicamentos: list[str]):
        if dni_paciente not in self.__pacientes or matricula_medico not in self.__medicos:
            raise ValueError("Datos inválidos")

        receta = Receta(
            self.__pacientes[dni_paciente],
            self.__medicos[matricula_medico],
            medicamentos
        )
        self.__historias_clinicas[dni_paciente].agregar_receta(receta)

    def obtener_historia_clinica(self, dni: str) -> HistoriaClinica:
        if dni not in self.__historias_clinicas:
            raise ValueError("Paciente no registrado")
        return self.__historias_clinicas[dni]