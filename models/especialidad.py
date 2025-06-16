class Especialidad:
    def __init__(self, nombre: str, dias_atencion: list[str]):
        self.__nombre = nombre
        self.__dias_atencion = [dia.lower() for dia in dias_atencion]  # Ej: ["lunes", "miércoles"]

    def atiende_dia(self, dia: str) -> bool:
        return dia.lower() in self.__dias_atencion

    def get_dias_atencion(self) -> list[str]:
        return self.__dias_atencion