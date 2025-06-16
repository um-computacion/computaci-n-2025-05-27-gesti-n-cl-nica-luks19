from .exceptions import MatriculaInvalidaException
from .especialidad import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str):
        self.__nombre = nombre
        self.__matricula = self.__validar_matricula(matricula)
        self.__especialidades = []  # Lista de objetos Especialidad

    def __validar_matricula(self, matricula: str) -> str:
        if not (matricula.startswith("MP-") and matricula[3:].isdigit()):
            raise MatriculaInvalidaException("Formato debe ser MP-12345")
        return matricula

    def obtener_matricula(self) -> str:
        return self.__matricula

    def agregar_especialidad(self, especialidad: Especialidad):
        if especialidad not in self.__especialidades:
            self.__especialidades.append(especialidad)

    def obtener_especialidades(self):
        return self.__especialidades