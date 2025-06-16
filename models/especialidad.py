class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        self.__tipo = tipo
        self.__dias = [dia.lower() for dia in dias]

    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in self.__dias 