from .paciente import Paciente
from .medico import Medico

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos

    def obtener_medicamentos(self) -> list[str]:
        return self.__medicamentos

    def __str__(self) -> str:
        return f"Receta para {self.__paciente.obtener_nombre()} por {self.__medico.obtener_nombre()}: {', '.join(self.__medicamentos)}"