INSTRUCCIONES DE USO

USO DE INTERFAZ

Para comenzar a usar el sistema, desde el directorio principal ejecuta:

python3 cli.py

Accederás a la interfaz principal, que te ofrece las siguientes opciones:

1. Agregar paciente
2. Agregar médico
3. Agregar especialidad a médico
4. Agendar turno
5. Emitir receta
6. Ver historia clínica
7. Ver todos los turnos
8. Ver todos los pacientes
9. Ver todos los médicos
0. Salir

Detalle de opciones

Agregar paciente: Ingresa '1', luego el nombre, DNI y fecha de nacimiento del paciente (formato: dd/mm/aaaa).

Agregar médico: Ingresa '2', luego el nombre, matrícula y especialidades del médico (puedes ingresar varias especialidades separadas por coma).

Agregar especialidad a médico: Ingresa '3', luego la matrícula del médico, el nombre de la especialidad y los días de atención (separados por coma).

Agendar turno: Ingresa '4', luego el DNI del paciente, la matrícula del médico y la fecha y hora del turno (formato: dd/mm/aaaa HH:MM). El turno solo se agenda si el médico atiende ese día.

Emitir receta: Ingresa '5', luego el DNI del paciente, la matrícula del médico y los medicamentos (separados por coma).

Ver historia clínica: Ingresa '6', luego el DNI del paciente para ver su historia clínica.

Ver todos los turnos: Ingresa '7' para listar todos los turnos registrados.

Ver todos los pacientes: Ingresa '8' para listar todos los pacientes registrados.

Ver todos los médicos: Ingresa '9' para listar todos los médicos registrados.

Salir: Ingresa '0' para salir del sistema.

USO DE TESTS

Para ejecutar los tests, desde el directorio principal usa:

python3 -m unittest tests/test_cli.py

python3 -m unittest tests/test_clinica.py

python3 -m unittest tests/test_paciente.py

python3 -m unittest tests/test_medico.py

python3 -m unittest tests/test_receta.py

python3 -m unittest tests/test_historia_clinica.py

python3 -m unittest tests/test_especialidad.py

Cada archivo de test cubre los siguientes casos:

test_cli.py:
- Prueba la interfaz de línea de comandos (CLI): agregar pacientes, médicos, especialidades, agendar turnos, emitir recetas y ver historias clínicas desde la CLI.

test_clinica.py:
- Agregar pacientes y médicos correctamente y errores por duplicados.
- Agendar turnos válidos y evitar turnos duplicados.
- Verificar excepciones por paciente/médico inexistente.
- Emitir recetas válidas y errores si paciente/médico no existen.
- Comprobar que la HistoriaClinica recoge correctamente turnos y recetas.

test_paciente.py:
- Registro exitoso de pacientes.
- Errores por DNI inválido, duplicado o datos faltantes.

test_medico.py:
- Registro exitoso de médicos.
- Errores por matrícula inválida, duplicada o datos faltantes.

test_receta.py:
- Emisión de recetas y errores por datos inválidos.

test_historia_clinica.py:
- Registro correcto de turnos y recetas en la historia clínica.
- Errores al pedir la historia clínica de un paciente no registrado.

test_especialidad.py:
- Agregado correcto de especialidades y validaciones de días.

Puedes ejecutar todos los tests juntos con:
python3 -m unittest discover tests

¡GRACIAS POR UTILIZAR EL SISTEMA DE GESTIÓN CLÍNICA!