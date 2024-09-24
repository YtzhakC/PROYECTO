from hashlib import sha256
from datetime import datetime, timedelta
from persistencia.persistencia import cargarEstudiantes, cargarModulos, guardarAsistencia, guardarDocentes, guardarEstudiantes, guardarGrupos, guardarModulos
archModulos = 'ACME/util/registroModulos.json'
modulos = cargarModulos(archModulos)
archEstudiantes = 'ACME/util/registroEstudiantes.json'
estudiantes = cargarEstudiantes(archEstudiantes)
def clear():
    print('\n'*100)


def login():
    key = 'SISGESA'
    pssw = str()
    user = {}
    user['user'] = input('Digite su nombre de usuario: \n-> ')
    print(f'Bienvenido a SISGESA {user["user"]}, tu contraseña predefinida es: SISGESA')
    while pssw != key:
        print('Bienvenido al programa, a continuación, digite su nombre de usuario y la contraseña.')
        pssw = input('Digite la contraseña: \n->')
        if pssw == key:
            print(f'Bienvenido, {user}.')
            return True
        else:
            print('La contraseña es incorrecta, intente nuevamente.')        

def codificarContrasena(password):
    password = sha256(password.encode('utf-8')).hexdigest()

def registroGrupos(grupos):
    print('Registrar Grupo:')
    grupo = {}
    codigoGrupo = input('Digite el codigo del grupo: \n-> ')
    if codigoGrupo not in grupos:
        grupo['nombreGrupo'] = input('Digite el nombre del grupo: \n-> ')
        grupo['siglaGrupo'] = input('Digite la sigla del grupo: \n-> ')
        if len(grupo['siglaGrupo']) > 1:
            print('Error, la sigla del grupo debe contener solo una letra.')
            grupo['siglaGrupo'] = input('Digite la sigla del grupo: \n-> ')

        grupos[codigoGrupo] = grupo
        print('Hecho! Se ha registrado exitosamente el grupo.')
        grupos = dict(sorted(grupos.items()))
        guardarGrupos(grupos)
    else:
        input('El código ya existe, presione cualquier tecla para volver al menú...')

def registroModulos(modulos):
    modulo = {}
    codigoModulo = input('Digite el codigo del módulo: \n-> ')
    if codigoModulo not in modulos:
        modulo['nombreModulo'] = input('Digite el nombre del módulo: \n-> ')
        modulo['duracionModulo'] = int(input('Digite la duración en semanas del módulo (Digite solo números): \n-> '))
        modulo['horaInicio'] = datetime.strptime(input('La hora de Inicio del modulo es:' ), '%H:%M')
        modulo['horaInicio'] = datetime.strftime(modulo['horaInicio'], '%H:%M')
        modulo['horaSalida'] = datetime.strptime(input('La hora de Salida del modulo es:' ), '%H:%M')
        modulo['horaSalida'] = datetime.strftime(modulo['horaSalida'], '%H:%M')
        modulos[codigoModulo] = modulo
        print('Hecho! Se ha registrado exitosamente el módulo.')
        modulos = dict(sorted(modulos.items()))
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
        estudiantes[codigoEstudiante] = estudiante
        print('Hecho! Se ha registrado exitosamente el estudiante.')
        estudiantes = dict(sorted(estudiantes.items()))
        guardarEstudiantes(estudiantes)
    else:
        input('El código ya existe, presione cualquier tecla para volver al menú...')

def asignarGruposyModulos():
    return

def registroDocentes(docentes):
    docente = {}
    cedulaDocente = input('Digite la cédula del docente: \n-> ')
    if cedulaDocente not in docentes:
        docente['nombreDocente'] = input('Digite el nombre del estudiante: \n-> ')
        docente['modulosDocente'] = input("Introduce los códigos separados por comas: ").split(',')
        docente['codigos'] = [codigo.strip() for codigo in docente['codigos']] # Limpia los espacios en blanco, si es que los hay.
        docentes = dict(sorted(docentes.items()))
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


def consultaInformacion():
    print('Consulta de Información')
    print('1. Consultar los estudiantes matriculados en un grupo.')
    print('2. Consultar los estudiantes inscritos en un módulo')
    print('3. Consultar los docentes que imparten un módulo.')
    print('4. Consultar los estudiantes a cargo de un docente en un módulo.')


def generacionInformes():

    return

def cambioContrasena(password):
    sw = True
    while sw:
        confirm_pass = input('Digite la contraseña actual: \n-> ')
        if confirm_pass == password:
            new_password = input('Digite la nueva contraseña: \n->' )
            password = new_password
    return

