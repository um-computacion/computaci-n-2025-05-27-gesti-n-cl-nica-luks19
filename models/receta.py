# receta.py
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
        return f"Receta {self.__fecha}: {', '.join(self.__medicamentos)}"