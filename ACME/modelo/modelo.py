from datetime import datetime, timedelta
from persistencia.persistencia import guardarAsistencia, guardarDocentes, guardarEstudiantes, guardarGrupos, guardarModulos, guardar_contra, cargar_contra, hash_contra, contra_predefinida
import getpass

estudiantes = {}
modulos = {}

def clear():
    print('\n'*100)

def login():
    input("Ingrese su nombre de usuario: ")
    contra = getpass.getpass("Ingrese su contraseña: ")
    if cargar_contra() is None: # Primera vez que se ejecuta el sistema
        if contra == contra_predefinida:
            guardar_contra(contra)
            print("Bienvenido al sistema")
            return True
        else:
            print("Contraseña incorrecta")
            return False
    elif hash_contra(contra) == cargar_contra():
        print("Bienvenido al sistema")
        return True
    else:
        print("Contraseña incorrecta")
        return False

 # Cambia la contraseña actual
def cambia_contra():
    actual_contra = getpass.getpass("Ingrese la contraseña actual: ")
    if hash_contra(actual_contra) == cargar_contra():
        nueva_contra = getpass.getpass("Ingrese la nueva contraseña: ")
        guardar_contra(nueva_contra)
        print("Contraseña cambiada con éxito")
    else:
        print("Contraseña incorrecta") 

def registroGrupos(grupos):
    print('Registrar Grupo:')
    grupo = {}
    codigoGrupo = input('Digite el codigo del grupo: \n-> ')
    if codigoGrupo not in grupos:
        nombreGrupo = input('Digite el nombre del grupo: \n-> ')
        siglasGrupo = input('Digite la sigla del grupo: \n-> ')
        if len(siglasGrupo) > 4:
            print('Error, las siglas del grupo deben contener hasta máximo 4 letras.')
        grupo = {
            'codigoGrupo':codigoGrupo,
            'nombreGrupo':nombreGrupo,
            'siglasGrupo':siglasGrupo,
        }

        grupos[codigoGrupo] = grupo
        print('Hecho! Se ha registrado exitosamente el grupo.')

        guardarGrupos(grupos)
    else:
        input('El código ya existe, volviendo al menú...')

def registroModulos(modulos):
    modulo = {}
    codigoModulo = input('Digite el codigo del módulo: \n-> ')
    if codigoModulo not in modulos:
        NombreModulo = input('Digite el nombre del módulo: \n-> ')
        DuracionModulo = int(input('Digite la duración en semanas del módulo (Digite solo números): \n-> '))
        HoraIniciar = datetime.strptime(input('La hora de Inicio del modulo es:' ), '%H:%M')
        HoraIniciar = datetime.strftime(HoraIniciar, '%H:%M')
        HoraFin = datetime.strptime(input('La hora de Salida del modulo es:' ), '%H:%M')
        HoraFin = datetime.strftime(HoraFin, '%H:%M')
        modulo = {
            'nombre':NombreModulo,
            'duracion':DuracionModulo,
            'horaInicio':HoraIniciar,
            'horaFin':HoraFin
        }
        modulos[codigoModulo] = modulo
        print('Hecho! Se ha registrado exitosamente el módulo.')
        guardarModulos(modulos)
    else:
        input('El código ya existe, presione cualquier tecla para volver al menú...')

def registroEstudiantes(estudiantes):
    estudiante = {}
    codigoEstudiante = input('Digite el codigo del estudiante: \n-> ')
    if codigoEstudiante not in estudiantes:
        estudiante['nombreEstudiante'] = input('Digite el nombre del estudiante: \n-> ')
        estudiante['edadEstudiante'] = input('Digite la edad del estudiante: \n-> ')
        estudiante['sexoEstudiante'] = input('Digite la sexo del estudiante: \n-> ').lower()
        if estudiante['sexoEstudiante'] == 'f' or estudiante['sexoEstudiante'] == 'm':
            pass
        else:
            print('Incorrecto, el sexo solo puede ser f o m')
        estudiante['grupo'] = input('Digite el grupo al que pertenece:  \n-> ')
        estudiante['modulosEstudiante'] = input('Digite los modulos del grupo hasta maximo 3 y separados por comas: \n-> ').split(',')
        estudiantes[codigoEstudiante] = estudiante
        print('Hecho! Se ha registrado exitosamente el estudiante.')
        estudiantes = dict(sorted(estudiantes.items()))
        guardarEstudiantes(estudiantes)
    else:
        input('El código ya existe, presione cualquier tecla para volver al menú...')

def registroDocentes(docentes):
    docente = {}
    cedulaDocente = input('Digite la cédula del docente: \n-> ')
    if cedulaDocente not in docentes:
        NombreDoc = input('Digite el nombre del estudiante: \n-> ')
        ModsDoc = input("Introduce los códigos separados por comas: ").split(',')
        docente = {
            'nombre':NombreDoc,
            'modulos':ModsDoc
        }
        docentes[cedulaDocente] = docente
        print('Hecho! Se ha registrado exitosamente el docente.')
        guardarDocentes(docentes)
    else:
        input('El código ya existe, presione cualquier tecla para volver al menú...')

# Función para convertir objetos datetime a cadenas
def convertir_tiempos_a_str(asistencia):
    for estudiante, clase in asistencia.items():
        if 'horaEntrada' in clase and isinstance(clase['horaEntrada'], datetime):
            clase['horaEntrada'] = clase['horaEntrada'].strftime('%H:%M')
        if 'horaSalida' in clase and isinstance(clase['horaSalida'], datetime):
            clase['horaSalida'] = clase['horaSalida'].strftime('%H:%M')
    return asistencia

def registroAsistencia(asistencia):
    codigoEstudiante = input('Digite su código: \n-> ')
    if codigoEstudiante not in estudiantes:
        print('El código del estudiante no está registrado.')
        return
    else:
        clase = {}
        codigoModulo = input('Digite el código del módulo: \n-> ')
        clase['codigoModulo'] = codigoModulo
        if clase['codigoModulo'] not in modulos:
            print('El código del módulo no existe.')
            return

        # Obtener hora de entrada del estudiante
        horaEntrada = datetime.strptime(input('La hora de entrada es: '), '%H:%M')
        clase['horaEntrada'] = horaEntrada

        # Obtener hora de salida del estudiante
        horaSalida = datetime.strptime(input('La hora de salida es: '), '%H:%M')
        clase['horaSalida'] = horaSalida

        # Verificar si el código del módulo tiene una hora de inicio registrada
        horaInicio = datetime.strptime(modulos[codigoModulo]['horaInicio'], '%H:%M')

        # Calcular la diferencia entre la hora de entrada y la hora de inicio
        diferenciaHora = horaEntrada - horaInicio

        # Verificar si la diferencia es mayor a 15 minutos
        if diferenciaHora > timedelta(minutes=15):
            clase['puntualidad'] = 'El estudiante llego con retardo'
        else:
            clase['puntualidad'] = 'El estudiante llego puntual.'

        # Registrar la asistencia del estudiante en el diccionario
        asistencia[codigoEstudiante] = clase
        asistencia = dict(sorted(asistencia.items()))

        # Convertir tiempos a cadenas antes de guardar
        asistencia = convertir_tiempos_a_str(asistencia)

        # Guardar la asistencia actualizada
        guardarAsistencia(asistencia)

        input('El código ya está registrado, presione cualquier tecla para volver al menú...')

def consulta_estudiantes_Por_Grupo(estudiantes, grupos):
    codigoGrupo = input('Digite el código del grupo: \n-> ')
    if codigoGrupo in grupos: 
        print('Estudiantes matriculados en el grupo:')
        for codigoEstudiante, datos in estudiantes.items():
            if datos.get('grupo') == codigoGrupo:
                print(f"Código: {codigoEstudiante}, Nombre: {datos['nombreEstudiante']}")
    else:
        print('El código del grupo no existe.')

def consulta_estudiantes_Por_Modulo(modulos, estudiantes):
    codigoModulo = input('Digite el código del módulo: \n')
    if codigoModulo in modulos:
        print('Estudiantes inscritos en el módulo:')
        for estudiante, datos in estudiantes.items():
            if datos.get('modulosEstudiante') and codigoModulo in datos['modulosEstudiante']:
                print(f"Código: {estudiante}, Nombre: {datos['nombreEstudiante']}")
    else:
        print('El código del módulo no existe.')

def consulta_Docentes_Por_Modulo(modulos, docentes):
    codigoModulo = input('Digite el código del módulo: \n-> ')
    if codigoModulo in modulos:
        print('Docentes que imparten el módulo:')
        for cedulaDocente, datos in docentes.items():
            if 'modulos' in datos and codigoModulo in datos['modulos']:
                nombre_docente = datos.get('nombre', 'Nombre no registrado')  # Si el nombre está vacío, muestra un mensaje por defecto
                print(f"Cédula: {cedulaDocente}, Nombre: {nombre_docente}")
    else:
        print('El código del módulo no existe.')

def consulta_Estudiantes_Por_Docente(estudiantes, docentes, modulos):
    cedulaDocente = input('Digite la cédula del docente: \n-> ')
    
    # Verificar si el docente está registrado
    if cedulaDocente in docentes:
        # Obtener los módulos asignados al docente
        modulos_docente = docentes[cedulaDocente].get('modulos', [])
        
        # Verificar si el docente tiene módulos asignados
        if not modulos_docente:
            print(f"El docente con cédula {cedulaDocente} no tiene módulos asignados.")
            return
        
        print(f"Estudiantes a cargo del docente con cédula {cedulaDocente}:")
        
        # Recorrer los estudiantes para encontrar aquellos inscritos en los módulos del docente
        for codigo_estudiante, datos_estudiante in estudiantes.items():
            modulos_estudiante = datos_estudiante.get('modulosEstudiante', [])
            
            # Encontrar módulos comunes entre el docente y el estudiante
            modulos_comunes = set(modulos_docente).intersection(set(modulos_estudiante))
            
            # Si hay módulos en común, mostrar la información del estudiante
            if modulos_comunes:
                nombre_estudiante = datos_estudiante.get('nombreEstudiante', 'Nombre no registrado')
                modulos_nombres = [modulos[modulo]['nombre'] for modulo in modulos_comunes]
                print(f"Código del estudiante: {codigo_estudiante}, Nombre: {nombre_estudiante}, Módulos comunes: {', '.join(modulos_nombres)}")
    
    else:
        print('La cédula del docente no existe.')

def consultaInformacion(estudiantes, modulos, grupos, docentes):
    while True:
        print("* Consulta Informacion *")
        print('''
                1. Consultar los estudiantes matriculados en un grupo. 
                2. Consultar los estudiantes inscritos en un módulo. 
                3. Consultar los docentes que imparten un módulo. 
                4. Consultar los estudiantes a cargo de un docente en un módulo. 
                5. Salir
              ''')
        opcion = input(">>> Opción: ").strip()
        match opcion:
            case "1":
                consulta_estudiantes_Por_Grupo(estudiantes, grupos) 
            case "2":
                consulta_estudiantes_Por_Modulo(modulos, estudiantes)
            case "3":
                consulta_Docentes_Por_Modulo(modulos, docentes) 
            case "4":
                consulta_Estudiantes_Por_Docente(estudiantes, docentes, modulos) 
            case '5':
                break
            case _:
                print("Opción no válida.")

def generacionInformes(asistencia, estudiantes, modulos):
    while True:
        print("* Consulta Informacion *")
        print('''
                1. Estudiantes que han llegado tarde a un módulo en un mes específico
                2. Estudiantes que se retiraron antes de la finalización de una sesión en un mes específico
                3. Estudiantes que no han faltado a ningún módulo durante un mes
                4. Porcentaje de asistencia por módulo
                5. Salir
              ''')
        opcion = input(">>> Opción: ").strip()
        match opcion:
            case "1":
                informe_tardanza(asistencia)
            case "2":
                informe_salida_temprana(asistencia)
            case "3":
                informe_asistencia_perfecta(asistencia, estudiantes) 
            case "4":
                informe_porcentaje_asistencia(asistencia, estudiantes, modulos)
            case '5':
                break
            case _:
                print("Opción no válida.")

def informe_tardanza(asistencia):
    mes_especifico = input("Digite el mes específico (MM): ")
    modulo_especifico = input("Digite el código del módulo: ")
    estudiantes_tarde = []
    for estudiante, clase in asistencia.items():
        if clase['codigoModulo'] == modulo_especifico and clase['horaEntrada'].month == int(mes_especifico):
            if clase['puntualidad'] == 'El estudiante llego con retardo':
                estudiantes_tarde.append(estudiante)
    print("Estudiantes que han llegado tarde a un módulo en un mes específico:")
    for estudiante in estudiantes_tarde:
        print(f"Código: {estudiante}, Nombre: {estudiantes[estudiante]['nombre']}")

def informe_salida_temprana(asistencia):
    mes_especifico = input("Digite el mes específico (MM): ")
    modulo_especifico = input("Digite el código del módulo: ")
    estudiantes_salida_temprana = []
    for estudiante, clase in asistencia.items():
        if clase['codigoModulo'] == modulo_especifico and clase['horaSalida'].month == int(mes_especifico):
            if clase['horaSalida'] < clase['horaFin']:
                estudiantes_salida_temprana.append(estudiante)
    print("Estudiantes que se retiraron antes de la finalización de una sesión en un mes específico:")
    for estudiante in estudiantes_salida_temprana:
        print(f"Código: {estudiante}, Nombre: {estudiantes[estudiante]['nombre']}")

def informe_asistencia_perfecta(asistencia, estudiantes):
    mes_especifico = input("Digite el mes específico (MM): ")
    estudiantes_perfectos = []
    for estudiante, datos in estudiantes.items():
        if all(clase['puntualidad'] == 'El estudiante llego puntual.' for clase in asistencia.values() if clase['codigoEstudiante'] == estudiante and clase['horaEntrada'].month == int(mes_especifico)):
            estudiantes_perfectos.append(estudiante)
    print("Estudiantes que no han faltado a ningún módulo durante un mes:")
    for estudiante in estudiantes_perfectos:
        print(f"Código: {estudiante}, Nombre: {estudiantes[estudiante]['nombreEstudiante']}")

def informe_porcentaje_asistencia(asistencia, estudiantes, modulos):
    modulo_especifico = input("Digite el código del módulo: ")
    total_estudiantes = len([estudiante for estudiante, datos in estudiantes.items() if modulo_especifico in datos['modulosEstudiante']])
    asistentes = len([clase for clase in asistencia.values() if clase['codigoModulo'] == modulo_especifico and clase['puntualidad'] == 'El estudiante llego puntual.'])
    if total_estudiantes == 0:
        print("No hay estudiantes inscritos en este módulo.")
    else:
        porcentaje_asistencia = (asistentes / total_estudiantes) * 100
        print(f"El porcentaje de asistencia del módulo {modulo_especifico} es {porcentaje_asistencia:.2f}%")