from models.clinica import Clinica
from models.paciente import Paciente
from models.medico import Medico
from models.especialidad import Especialidad
from datetime import datetime

class CLI:
    def __init__(self):
        self.__clinica = Clinica()

    def __agregar_paciente(self):
        nombre = input("Nombre: ")
        dni = input("DNI: ")
        fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
        paciente = Paciente(nombre, dni, fecha_nacimiento)
        self.__clinica.agregar_paciente(paciente)
        print("Paciente registrado con éxito!")

    def __agregar_medico(self):
        nombre = input("Nombre del médico: ")
        matricula = input("Matrícula: ")
        especialidades_input = input("Especialidades (separadas por coma): ")
        especialidades = [esp.strip() for esp in especialidades_input.split(",") if esp.strip()]
        medico = Medico(nombre, matricula, especialidades)
        self.__clinica.agregar_medico(medico)
        print("Médico registrado con éxito!")

    def __agregar_especialidad(self):
        matricula = input("Matrícula del médico: ")
        nombre_especialidad = input("Nombre de la especialidad: ")
        dias_input = input("Días de atención (separados por coma): ")
        dias = [d.strip() for d in dias_input.split(",") if d.strip()]
        especialidad = Especialidad(nombre_especialidad, dias)
        self.__clinica.agregar_especialidad_a_medico(matricula, especialidad)
        print("Especialidad agregada con éxito!")

    def __agendar_turno(self):
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        fecha_hora = input("Fecha y hora (dd/mm/aaaa HH:MM): ")
        try:
            fecha = datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M")
            self.__clinica.agendar_turno(dni, matricula, fecha)
            print("Turno agendado con éxito!")
        except ValueError as e:
            print(f"Error en el formato de fecha: {e}")

    def __emitir_receta(self):
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        medicamentos_input = input("Medicamentos (separados por coma): ")
        medicamentos = [m.strip() for m in medicamentos_input.split(",") if m.strip()]
        try:
            self.__clinica.emitir_receta(dni, matricula, medicamentos)
            print("Receta emitida con éxito!")
        except Exception as e:
            print(f"Error al emitir receta: {e}")

    def __ver_historia_clinica(self):
        dni = input("Ingrese el DNI del paciente: ")
        try:
            historia_clinica = self.__clinica.obtener_historia_clinica(dni)
            print("\n" + str(historia_clinica))

            recetas = historia_clinica.obtener_recetas()
            if recetas:
                print("\nRecetas:")
                for i, receta in enumerate(recetas, 1):
                    print(f"{i}. {receta}")
            else:
                print("\nNo hay recetas registradas.")

            turnos = historia_clinica.obtener_turnos()
            if turnos:
                print("\nTurnos:")
                for i, turno in enumerate(turnos, 1):
                    print(f"{i}. {turno}")
            else:
                print("\nNo hay turnos registrados.")

        except Exception as e:
            print(f"\nError: {e}")

    def __ver_todos_los_turnos(self):
        turnos = self.__clinica.obtener_turnos()
        if turnos:
            print("\nTurnos registrados:")
            for i, turno in enumerate(turnos, 1):
                print(f"{i}. {turno}")
        else:
            print("\nNo hay turnos registrados.")

    def __ver_todos_los_pacientes(self):
        pacientes = self.__clinica.obtener_pacientes()
        if pacientes:
            print("\nPacientes registrados:")
            for i, paciente in enumerate(pacientes, 1):
                print(f"{i}. {paciente}")
        else:
            print("\nNo hay pacientes registrados.")

    def __ver_todos_los_medicos(self):
        medicos = self.__clinica.obtener_medicos()
        if medicos:
            print("\nMédicos registrados:")
            for i, medico in enumerate(medicos, 1):
                print(f"{i}. {medico}")
        else:
            print("\nNo hay médicos registrados.")

    def ejecutar(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Agregar paciente")
            print("2. Agregar médico")
            print("3. Agregar especialidad a médico")
            print("4. Agendar turno")
            print("5. Emitir receta")
            print("6. Ver historia clínica")
            print("7. Ver todos los turnos")
            print("8. Ver todos los pacientes")
            print("9. Ver todos los médicos")
            print("0. Salir")
            
            try:
                opcion = input("Seleccione una opción: ")
                
                if opcion == "1":
                    self.__agregar_paciente()
                elif opcion == "2":
                    self.__agregar_medico()
                elif opcion == "3":
                    self.__agregar_especialidad()
                elif opcion == "4":
                    self.__agendar_turno()
                elif opcion == "5":
                    self.__emitir_receta()
                elif opcion == "6":
                    self.__ver_historia_clinica()
                elif opcion == "7":
                    self.__ver_todos_los_turnos()
                elif opcion == "8":
                    self.__ver_todos_los_pacientes()
                elif opcion == "9":
                    self.__ver_todos_los_medicos()
                elif opcion == "0":
                    print("¡Gracias por utilizar el sistema de gestión clínica!")
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
            
            except Exception as e:
                print(f"\nOcurrió un error: {e}\nPor favor, intente nuevamente.")

if __name__ == "__main__":
    cli = CLI()
    cli.ejecutar()