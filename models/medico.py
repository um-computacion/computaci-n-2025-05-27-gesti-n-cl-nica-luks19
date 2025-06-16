from .exceptions import MatriculaInvalidaException
from .especialidad import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str):
        self.__nombre = nombre
        self.__matricula = self.__validar_matricula(matricula)
        self.__especialidades = []

    def __validar_matricula(self, matricula: str) -> str:
        if not (matricula.startswith("MP-") and matricula[3:].isdigit()):
            raise MatriculaInvalidaException("Formato debe ser MP-12345")
        return matricula

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_matricula(self) -> str:
        return self.__matricula

    def agregar_especialidad(self, especialidad: Especialidad):
        if especialidad not in self.__especialidades:
            self.__especialidades.append(especialidad)

    def obtener_especialidades(self) -> list[Especialidad]:
        return self.__especialidades

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for especialidad in self.__especialidades:
            if especialidad.atiende_dia(dia.lower()):
                return str(especialidad)
        return None

    def __str__(self) -> str:
        especialidades_str = ", ".join([str(esp) for esp in self.__especialidades])
        return f"Médico: {self.__nombre} (Matrícula: {self.__matricula}) - Especialidades: {especialidades_str}"