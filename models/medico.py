from models.exceptions import MatriculaInvalidaException

class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: list = None):
        if not self.__validar_matricula(matricula):
            raise MatriculaInvalidaException(f"Formato de matrícula inválido: {matricula}")
            
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = especialidades if especialidades else []

    def __validar_matricula(self, matricula: str) -> bool:
        parts = matricula.split("-")
        return (len(parts) == 2 and 
                parts[0] == "MP" and 
                parts[1].isdigit() and 
                len(parts[1]) >= 3)

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidades(self) -> list:
        return self.__especialidades

    def agregar_especialidad(self, especialidad: str):
        if especialidad not in self.__especialidades:
            self.__especialidades.append(especialidad)

    def __str__(self):
        especialidades = ", ".join(self.__especialidades) if self.__especialidades else "Ninguna"
        return f"{self.__nombre} (Matrícula: {self.__matricula}) - Especialidades: {especialidades}"

    def __repr__(self):
        return f"Medico(nombre={self.__nombre}, matricula={self.__matricula}, especialidades={self.__especialidades})"