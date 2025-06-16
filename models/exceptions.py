class ClinicaException(Exception):
    """Excepción base para errores de la clínica."""
    def __init__(self, message="Ha ocurrido un error en la clínica."):
        super().__init__(message)

class PacienteNoEncontrado(ClinicaException):
    def __init__(self, message="El paciente requerido NO existe."):
        super().__init__(message)

class MedicoNoDisponible(ClinicaException):
    def __init__(self, message="El médico solicitado no está disponible."):
        super().__init__(message)

class TurnoOcupado(ClinicaException):
    def __init__(self, message="El turno solicitado ya está ocupado."):
        super().__init__(message)

class RecetaInvalida(ClinicaException):
    def __init__(self, message="La receta ingresada es inválida."):
        super().__init__(message)

class TurnoExiste(ClinicaException):
    def __init__(self, message="El turno que intentas ingresar ya existe."):
        super().__init__(message)

class FormatoIncorrecto(ClinicaException):
    def __init__(self, message="El formato de la fecha fue ingresado incorrectamente."):
        super().__init__(message)

class ValorIncorrecto(ClinicaException):
    def __init__(self, message="Debes introducir un número!"):
        super().__init__(message)