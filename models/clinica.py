from datetime import datetime
from .paciente import Paciente
from .medico import Medico
from .turno import Turno
from .historia_clinica import HistoriaClinica
from .receta import Receta
from .especialidad import Especialidad 
from .exceptions import (
    PacienteExistenteException,
    MedicoExistenteException,
    PacienteNoEncontrado,
    MedicoNoDisponible,
    TurnoOcupado
)

# Diccionario para traducir días de la semana de inglés a español
DIAS_SEMANA = {
    "monday": "lunes",
    "tuesday": "martes",
    "wednesday": "miércoles",
    "thursday": "jueves",
    "friday": "viernes",
    "saturday": "sábado",
    "sunday": "domingo"
}

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

    def agendar_turno(self, dni: str, matricula: str, fecha_hora: datetime):
        # Validar existencia
        if dni not in self.__pacientes:
            raise PacienteNoEncontrado("Paciente no registrado")
        if matricula not in self.__medicos:
            raise MedicoNoDisponible("Médico no registrado")
        # (Opcional) No agendar turnos en el pasado
        if fecha_hora < datetime.now():
            raise ValueError("No se puede agendar un turno en el pasado.")

        # Evitar turnos duplicados (mismo médico y hora)
        for turno in self.__turnos:
            if (turno.obtener_medico().obtener_matricula() == matricula and
                turno.obtener_fecha_hora() == fecha_hora):
                raise TurnoOcupado("El turno solicitado ya está ocupado.")

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        # Si usas especialidad, puedes adaptarlo aquí
        especialidad = "Consulta general"
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        if dni not in self.__pacientes:
            raise PacienteNoEncontrado("Paciente no registrado")
        if matricula not in self.__medicos:
            raise MedicoNoDisponible("Médico no registrado")
        receta = Receta(
            self.__pacientes[dni],
            self.__medicos[matricula],
            medicamentos
        )
        self.__historias_clinicas[dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni: str) -> HistoriaClinica:
        if dni not in self.__historias_clinicas:
            raise PacienteNoEncontrado("Paciente no registrado")
        return self.__historias_clinicas[dni]

    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos