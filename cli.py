from models.clinica import Clinica
from models.paciente import Paciente
from models.medico import Medico
from models.especialidad import Especialidad
from datetime import datetime

class CLI:
    def __init__(self):
        self.__clinica = Clinica()

    def mostrar_menu(self):
        print("\n--- Menú Clínica ---")
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

    def iniciar(self):
        while True:
            self.mostrar_menu()
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
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def __agregar_paciente(self):
        try:
            nombre = input("Nombre: ")
            dni = input("DNI: ")
            fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
            paciente = Paciente(nombre, dni, fecha_nacimiento)
            self.__clinica.agregar_paciente(paciente)
            print("Paciente registrado con éxito!")
        except Exception as e:
            print(f"Error: {e}")

    def __agregar_medico(self):
        try:
            nombre = input("Nombre: ")
            matricula = input("Matrícula: ")
            medico = Medico(nombre, matricula)
            self.__clinica.agregar_medico(medico)
            print("Médico registrado con éxito!")
        except Exception as e:
            print(f"Error: {e}")

    def __agregar_especialidad(self):
        try:
            matricula = input("Matrícula del médico: ")
            nombre_especialidad = input("Nombre de la especialidad: ")
            dias_atencion = input("Días de atención (separados por coma, ej: lunes,miercoles): ").split(',')
            especialidad = Especialidad(nombre_especialidad, dias_atencion)
            self.__clinica.agregar_especialidad_a_medico(matricula, especialidad)
            print("Especialidad agregada con éxito!")
        except Exception as e:
            print(f"Error: {e}")

    def __agendar_turno(self):
        try:
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            fecha = input("Fecha (dd/mm/aaaa HH:MM): ")
            fecha_dt = datetime.strptime(fecha, "%d/%m/%Y %H:%M")
            self.__clinica.agendar_turno(dni, matricula, fecha_dt)
            print("Turno agendado con éxito!")
        except Exception as e:
            print(f"Error: {e}")

    def __emitir_receta(self):
        try:
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            medicamentos = input("Medicamentos (separados por coma, ej: Paracetamol,Ibuprofeno): ").split(',')
            self.__clinica.emitir_receta(dni, matricula, medicamentos)
            print("Receta emitida con éxito!")
        except Exception as e:
            print(f"Error: {e}")

    def __ver_historia_clinica(self):
        try:
            dni = input("DNI del paciente: ")
            historia_clinica = self.__clinica.obtener_historia_clinica(dni)
            print(str(historia_clinica))
            recetas = historia_clinica.get_recetas()
            if recetas:
                print("\nRecetas:")
                for receta in recetas:
                    print(receta)
            else:
                print("\nNo hay recetas registradas.")
            turnos = historia_clinica.get_turnos()
            if turnos:
                print("\nTurnos:")
                for turno in turnos:
                    print(turno)
            else:
                print("\nNo hay turnos registrados.")
        except Exception as e:
            print(f"Error: {e}")

    def __ver_todos_los_turnos(self):
        try:
            turnos = self.__clinica.obtener_turnos()
            if turnos:
                print("\n--- Todos los turnos ---")
                for turno in turnos:
                    print(turno)
            else:
                print("No hay turnos registrados.")
        except Exception as e:
            print(f"Error: {e}")

    def __ver_todos_los_pacientes(self):
        try:
            pacientes = self.__clinica.obtener_pacientes()
            if pacientes:
                print("\n--- Todos los pacientes ---")
                for paciente in pacientes:
                    print(paciente)
            else:
                print("No hay pacientes registrados.")
        except Exception as e:
            print(f"Error: {e}")

    def __ver_todos_los_medicos(self):
        try:
            medicos = self.__clinica.obtener_medicos()
            if medicos:
                print("\n--- Todos los médicos ---")
                for medico in medicos:
                    print(medico)
            else:
                print("No hay médicos registrados.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    cli = CLI()
    cli.iniciar()