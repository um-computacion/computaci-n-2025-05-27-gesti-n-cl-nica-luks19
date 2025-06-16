from datetime import datetime
from .paciente import Paciente
from .medico import Medico

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self) -> str:
        medicamentos_str = ", ".join(self.__medicamentos)
        fecha_str = self.__fecha.strftime("%d/%m/%Y %H:%M")
        return (f"Receta emitida el {fecha_str}\n"
                f"Paciente: {self.__paciente.obtener_nombre()}\n"
                f"Médico: {self.__medico.obtener_nombre()}\n"
                f"Medicamentos: {medicamentos_str}")