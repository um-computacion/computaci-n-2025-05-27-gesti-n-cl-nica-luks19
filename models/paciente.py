from .exceptions import ClinicaException

class DNIInvalidoException(ClinicaException):
    pass

class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        self.__nombre = nombre
        self.__dni = self.__validar_dni(dni)
        self.__fecha_nacimiento = fecha_nacimiento

    def __validar_dni(self, dni: str) -> str:
        if not (dni.isdigit() and len(dni) == 8):
            raise DNIInvalidoException("DNI debe tener 8 dígitos numéricos.")
        return dni

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_dni(self) -> str:
        return self.__dni

    def obtener_fecha_nacimiento(self) -> str:
        return self.__fecha_nacimiento

    def __str__(self) -> str:
        return f"Paciente: {self.__nombre} (DNI: {self.__dni}, Fecha de Nacimiento: {self.__fecha_nacimiento})"