from datetime import datetime
from .paciente import Paciente
from .medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad

    def obtener_paciente(self) -> Paciente:
        return self.__paciente

    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def obtener_especialidad(self) -> str:
        return self.__especialidad

    def __str__(self) -> str:
        fecha_str = self.__fecha_hora.strftime("%d/%m/%Y %H:%M") if isinstance(self.__fecha_hora, datetime) else str(self.__fecha_hora)
        return (f"Turno de {self.__especialidad} para {self.__paciente.obtener_nombre()} "
                f"con {self.__medico.obtener_nombre()} el {fecha_str}")
    
    