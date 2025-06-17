
class HistoriaClinica:
    def __init__(self, paciente):
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []

    def agregar_turno(self, turno):
        self.__turnos.append(turno)

    def agregar_receta(self, receta):
        self.__recetas.append(receta)

    def obtener_turnos(self):
        return self.__turnos

    def obtener_recetas(self):
        return self.__recetas

    def __str__(self):
        return f"Historia de {self.__paciente.obtener_nombre()} (DNI: {self.__paciente.obtener_dni()}): {len(self.__turnos)} turnos, {len(self.__recetas)} recetas"