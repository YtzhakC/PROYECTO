import json
from pathlib import Path
import  os
import  hashlib

contra_predefinida = "SISGESA"
archivo_contra= "password.txt"
def hash_contra(contra):   #Encriptar la contraseña usando SHA-256
    sha256 = hashlib.sha256()
    sha256.update(contra.encode("utf-8"))
    return sha256.hexdigest()

def guardar_contra(contra): #Guarda la contraseña encriptada en un archivo
    with open(archivo_contra, "w") as file:
        file.write(hash_contra(contra))

def cargar_contra(): #Carga la contraseña encriptada del archivo
    if os.path.exists(archivo_contra):
        with open(archivo_contra, "r") as file:
            return file.read()
    else:
        return None

def guardarGrupos(grupos):
    with open('ACME/util/registroGrupos.json', 'w') as file:
        json.dump(grupos, file, indent=4)

    if not file.closed:
        file.close()

def guardarModulos(modulo):
    with open('ACME/util/registroModulos.json', 'w') as file:
        json.dump(modulo, file, indent=4)

    if not file.closed:
        file.close()

def guardarEstudiantes(estudiante):
    with open('ACME/util/registroEstudiantes.json', 'w') as file:
        json.dump(estudiante, file, indent=4)

    if not file.closed:
        file.close()

def guardarDocentes(docente):
    with open('ACME/util/registroDocentes.json', 'w') as file:
        json.dump(docente, file, indent=4)

    if not file.closed:
        file.close()

def guardarAsistencia(asistencia):
    with open('ACME/util/registroAsistencia.json', 'w') as file:
        json.dump(asistencia , file, indent=4)

    if not file.closed:
        file.close()

def cargarGrupos(arch):
    archivo = Path(arch)
    grupos = {}

    if archivo.is_file():
        try:
            if archivo.stat().st_size == 0:
                print('>>> El archivo de grupos está vacío. Iniciando con datos vacíos.')
                grupos = {}
            else:
                with open(arch, 'r') as file:
                    grupos = json.load(file)
        except json.JSONDecodeError:
            print('>>> Error de formato JSON en grupos. Iniciando con datos vacíos.')
            grupos = {}
        except Exception as e:
            print(f'>>> Error al abrir el archivo de grupos: {e}')
            grupos = {}
    else:
        print('>>> El archivo de grupos no existe. Creando uno nuevo.')
        grupos = {}
        with open(arch, 'w') as file:
            json.dump(grupos, file)

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
                with open(arch, 'r') as file:
                    docentes = json.load(file)
        except json.JSONDecodeError:
            print('>>> Error de formato JSON en docentes. Iniciando con datos vacíos.')
            docentes = {}
        except Exception as e:
            print(f'>>> Error al abrir el archivo de docentes: {e}')
            docentes = {}
    else:
        print('>>> El archivo de docentes no existe. Creando uno nuevo.')
        docentes = {}
        with open(arch, 'w') as file:
            json.dump(docentes, file)

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
                with open(arch, 'r') as file:
                    modulos = json.load(file)
        except json.JSONDecodeError:
            print('>>> Error de formato JSON en módulos. Iniciando con datos vacíos.')
            modulos = {}
        except Exception as e:
            print(f'>>> Error al abrir el archivo de módulos: {e}')
            modulos = {}
    else:
        print('>>> El archivo de módulos no existe. Creando uno nuevo.')
        modulos = {}
        with open(arch, 'w') as file:
            json.dump(modulos, file)

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
                with open(arch, 'r') as file:
                    estudiantes = json.load(file)
        except json.JSONDecodeError:
            print('>>> Error de formato JSON en estudiantes. Iniciando con datos vacíos.')
            estudiantes = {}
        except Exception as e:
            print(f'>>> Error al abrir el archivo de estudiantes: {e}')
            estudiantes = {}
    else:
        print('>>> El archivo de estudiantes no existe. Creando uno nuevo.')
        estudiantes = {}
        with open(arch, 'w') as file:
            json.dump(estudiantes, file)

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
                with open(arch, 'r') as file:
                    asistencia = json.load(file)
        except json.JSONDecodeError:
            print('>>> Error de formato JSON en asistencia. Iniciando con datos vacíos.')
            asistencia = {}
        except Exception as e:
            print(f'>>> Error al abrir el archivo de asistencia: {e}')
            asistencia = {}
    else:
        print('>>> El archivo de asistencia no existe. Creando uno nuevo.')
        asistencia = {}
        with open(arch, 'w') as file:
            json.dump(asistencia, file)

    return asistencia