class ClinicaException(Exception):
    pass

class MatriculaInvalidaException(ClinicaException):
    pass

class ClinicaException(Exception):
    pass

# ... (las que ya tenías)
class PacienteExistenteException(ClinicaException):
    pass

class MedicoExistenteException(ClinicaException):
    pass

class TurnoOcupadoException(ClinicaException):
    pass