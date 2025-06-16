class ClinicaException(Exception):
    pass

class MatriculaInvalidaException(ClinicaException):
    pass

class PacienteExistenteException(ClinicaException):
    pass

class MedicoExistenteException(ClinicaException):
    pass

class TurnoOcupadoException(ClinicaException):
    pass