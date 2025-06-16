class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: list[str]):
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = especialidades  # lista de strings

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidades(self) -> list[str]:
        return self.__especialidades

    def __str__(self) -> str:
        especialidades_str = ", ".join(self.__especialidades)
        return f"Médico: {self.__nombre} (Matrícula: {self.__matricula}, Especialidades: {especialidades_str})"