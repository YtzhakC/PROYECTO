import json
from pathlib import Path

def guardarGrupos(grupos):
    with open('C:/Users/ytzha/OneDrive/Escritorio/PROYECTO/ACME/util/registroGrupos.json', 'w') as fd:
        json.dump(grupos, fd, indent=4)

    if not fd.closed:
        fd.close()

def guardarModulos(modulo):
    with open('ACME/util/registroModulos.json', 'w') as fd:
        json.dump(modulo, fd, indent=4)

    if not fd.closed:
        fd.close()

def guardarEstudiantes(estudiante):
    with open('ACME/util/registroEstudiantes.json', 'w') as fd:
        json.dump(estudiante, fd, indent=4)

    if not fd.closed:
        fd.close()

def guardarDocentes(docente):
    with open('ACME/util/registroDocentes.json', 'w') as fd:
        json.dump(docente, fd, indent=4)

    if not fd.closed:
        fd.close()

def guardarAsistencia(asistencia):
    with open('ACME/util/registroAsistencia.json', 'w') as fd:
        json.dump(asistencia , fd, indent=4)

    if not fd.closed:
        fd.close()

def cargarGrupos(arch):
    archivo = Path(arch)
    grupos = {}

    if archivo.is_file():
        try:
            if archivo.stat().st_size == 0:
                print('>>> El archivo de grupos está vacío. Iniciando con datos vacíos.')
                grupos = {}
            else:
                with open(arch, 'r') as fd:
                    grupos = json.load(fd)
        except json.JSONDecodeError:
            print('>>> Error de formato JSON en grupos. Iniciando con datos vacíos.')
            grupos = {}
        except Exception as e:
            print(f'>>> Error al abrir el archivo de grupos: {e}')
            grupos = {}
    else:
        print('>>> El archivo de grupos no existe. Creando uno nuevo.')
        grupos = {}
        with open(arch, 'w') as fd:
            json.dump(grupos, fd)

    return grupos

def cargarDocentes(arch):
    archivo = Path(arch)
    docentes = {}

    if archivo.is_file():
        try:
            if archivo.stat().st_size == 0:
                print('>>> El archivo de docentes está vacío. Iniciando con datos vacíos.')
                docentes = {}
            else:
                with open(arch, 'r') as fd:
                    docentes = json.load(fd)
        except json.JSONDecodeError:
            print('>>> Error de formato JSON en docentes. Iniciando con datos vacíos.')
            docentes = {}
        except Exception as e:
            print(f'>>> Error al abrir el archivo de docentes: {e}')
            docentes = {}
    else:
        print('>>> El archivo de docentes no existe. Creando uno nuevo.')
        docentes = {}
        with open(arch, 'w') as fd:
            json.dump(docentes, fd)

    return docentes

def cargarModulos(arch):
    archivo = Path(arch)
    modulos = {}

    if archivo.is_file():
        try:
            if archivo.stat().st_size == 0:
                print('>>> El archivo de módulos está vacío. Iniciando con datos vacíos.')
                modulos = {}
            else:
                with open(arch, 'r') as fd:
                    modulos = json.load(fd)
        except json.JSONDecodeError:
            print('>>> Error de formato JSON en módulos. Iniciando con datos vacíos.')
            modulos = {}
        except Exception as e:
            print(f'>>> Error al abrir el archivo de módulos: {e}')
            modulos = {}
    else:
        print('>>> El archivo de módulos no existe. Creando uno nuevo.')
        modulos = {}
        with open(arch, 'w') as fd:
            json.dump(modulos, fd)

    return modulos

def cargarEstudiantes(arch):
    archivo = Path(arch)
    estudiantes = {}

    if archivo.is_file():
        try:
            if archivo.stat().st_size == 0:
                print('>>> El archivo de estudiantes está vacío. Iniciando con datos vacíos.')
                estudiantes = {}
            else:
                with open(arch, 'r') as fd:
                    estudiantes = json.load(fd)
        except json.JSONDecodeError:
            print('>>> Error de formato JSON en estudiantes. Iniciando con datos vacíos.')
            estudiantes = {}
        except Exception as e:
            print(f'>>> Error al abrir el archivo de estudiantes: {e}')
            estudiantes = {}
    else:
        print('>>> El archivo de estudiantes no existe. Creando uno nuevo.')
        estudiantes = {}
        with open(arch, 'w') as fd:
            json.dump(estudiantes, fd)

    return estudiantes

def cargarAsistencia(arch):
    archivo = Path(arch)
    asistencia = {}

    if archivo.is_file():
        try:
            if archivo.stat().st_size == 0:
                print('>>> El archivo de asistencia está vacío. Iniciando con datos vacíos.')
                asistencia = {}
            else:
                with open(arch, 'r') as fd:
                    asistencia = json.load(fd)
        except json.JSONDecodeError:
            print('>>> Error de formato JSON en asistencia. Iniciando con datos vacíos.')
            asistencia = {}
        except Exception as e:
            print(f'>>> Error al abrir el archivo de asistencia: {e}')
            asistencia = {}
    else:
        print('>>> El archivo de asistencia no existe. Creando uno nuevo.')
        asistencia = {}
        with open(arch, 'w') as fd:
            json.dump(asistencia, fd)

    return asistencia
