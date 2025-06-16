from .exceptions import MatriculaInvalidaException

class Medico:
    def __init__(self, nombre: str, matricula: str):
        self.__nombre = nombre
        self.__matricula = self.__validar_matricula(matricula)
        self.__especialidades = []

    def __validar_matricula(self, matricula: str) -> str:
        if not (matricula.startswith("MP-") and matricula[3:].isdigit()):
            raise MatriculaInvalidaException("Formato debe ser MP-12345")
        return matricula

    def obtener_matricula(self) -> str:
        return self.__matricula