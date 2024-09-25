from modelo.modelo import clear, registroGrupos, registroModulos,\
 registroEstudiantes, registroDocentes, registroAsistencia, consultaInformacion,\
generacionInformes, login, cambia_contra
from persistencia.persistencia import cargarGrupos, cargarModulos,\
      cargarEstudiantes, cargarAsistencia, cargarDocentes


def menu():
    print('a. Registro de grupos.')
    print('')
    print('b. Registro de módulos.')
    print('')
    print('c. Registro de estudiantes.')
    print('')
    print('d. Registro de docentes.')
    print('')
    print('e. Registro de asistencia.')
    print('')
    print('f. Consultas de información')
    print('')
    print('g. Generación de informes')
    print('')
    print('h. Cambio de contraseña.')
    print('')
    print('i. Salida del sistema.')
    print('')
    


def ACME():
    if login() is True:
        sw = True
        while sw:
            clear()
            print("""
+=======================================================+
| ██████   ██████ ██████████ ██████   █████ █████  █████|
|░░██████ ██████ ░░███░░░░░█░░██████ ░░███ ░░███  ░░███ |
| ░███░█████░███  ░███  █ ░  ░███░███ ░███  ░███   ░███ |
| ░███░░███ ░███  ░██████    ░███░░███░███  ░███   ░███ |
| ░███ ░░░  ░███  ░███░░█    ░███ ░░██████  ░███   ░███ |
| ░███      ░███  ░███ ░   █ ░███  ░░█████  ░███   ░███ |
| █████     █████ ██████████ █████  ░░█████ ░░████████  |
|░░░░░     ░░░░░ ░░░░░░░░░░ ░░░░░    ░░░░░   ░░░░░░░░   |
+=======================================================+
      """)
            menu()
            op = input('Digite una opción: ')
            match op:
                case 'a':
                    clear()
                    print("""
+===================================================================+
| ██████   █████ █████  █████ ██████████ █████   █████    ███████   |
|░░██████ ░░███ ░░███  ░░███ ░░███░░░░░█░░███   ░░███   ███░░░░░███ |
| ░███░███ ░███  ░███   ░███  ░███  █ ░  ░███    ░███  ███     ░░███|
| ░███░░███░███  ░███   ░███  ░██████    ░███    ░███ ░███      ░███|
| ░███ ░░██████  ░███   ░███  ░███░░█    ░░███   ███  ░███      ░███|
| ░███  ░░█████  ░███   ░███  ░███ ░   █  ░░░█████░   ░░███     ███ |
| █████  ░░█████ ░░████████   ██████████    ░░███      ░░░███████░  |
|░░░░░    ░░░░░   ░░░░░░░░   ░░░░░░░░░░      ░░░         ░░░░░░░    |
|                                                                   |
|                                                                   |
|                                                                   |
|   █████████  ███████████   █████  █████ ███████████     ███████   |
|  ███░░░░░███░░███░░░░░███ ░░███  ░░███ ░░███░░░░░███  ███░░░░░███ |
| ███     ░░░  ░███    ░███  ░███   ░███  ░███    ░███ ███     ░░███|
|░███          ░██████████   ░███   ░███  ░██████████ ░███      ░███|
|░███    █████ ░███░░░░░███  ░███   ░███  ░███░░░░░░  ░███      ░███|
|░░███  ░░███  ░███    ░███  ░███   ░███  ░███        ░░███     ███ |
| ░░█████████  █████   █████ ░░████████   █████        ░░░███████░  |
|  ░░░░░░░░░  ░░░░░   ░░░░░   ░░░░░░░░   ░░░░░           ░░░░░░░    |
+===================================================================+
                          """)
                    grupos = {}
                    archGrupos = 'ACME/util/registroGrupos.json'
                    grupos = cargarGrupos(archGrupos)
                    grupos = registroGrupos(grupos)
                    clear()
                case 'b':
                    clear()
                    modulos = {}
                    archModulos = 'ACME/util/registroModulos.json'
                    modulos = cargarModulos(archModulos)
                    modulos = registroModulos(modulos)
                    clear()
                case 'c':
                    clear()
                    estudiantes = {}
                    archEstudiantes = 'ACME/util/registroEstudiantes.json'
                    estudiantes = cargarEstudiantes(archEstudiantes)
                    estudiantes = registroEstudiantes(estudiantes)
                    clear()
                case 'd':
                    clear()
                    docentes = {}
                    archDocentes = 'ACME/util/registroDocentes.json'
                    docentes = cargarDocentes(archDocentes)
                    docentes = registroDocentes(docentes)
                    clear()
                case 'e':
                    clear()
                    asistencia = {}
                    archAsistencia = 'ACME/util/registroAsistencia.json'
                    asistencia = cargarAsistencia(archAsistencia)
                    asistencia = registroAsistencia(asistencia)
                    clear()
                case 'f':
                    clear()
                    consultaInformacion()
                    clear()
                case 'g':
                    clear()
                    generacionInformes()
                    clear()
                case 'h':
                    clear()
                    cambia_contra()
                    clear()
                case 'i':
                    clear()
                    print('Gracias por usar el sistema... Adiós.')
                    break
