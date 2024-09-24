# # from hashlib import sha256
# # def codificarContrasena(password):
# #     password = sha256(password.encode('utf-8')).hexdigest()
# #     # print(password)
        
# from datetime import datetime, timedelta

# now = datetime.now()
# print(now)

# current_time = now.strftime('%H:%M:%S')

# print('\n')
# print(current_time)

# import json
# import os

# def registro_grupo():
#     grupo = {}
#     codigo = input("Ingrese el código del grupo: \n")
#     grupo["codigo"] = codigo
#     grupo["nombre"] = input("Ingrese el nombre del grupo:  \n")
#     grupo["sigla"] = input("Ingrese la sigla del grupo:  \n")

#     # Ruta completa del archivo JSON en la carpeta 'data'
#     archivo_json = os.path.join('data', 'grupo.json')

#     # Leer el archivo JSON y deserializarlo a un diccionario
#     try:
#         with open(archivo_json, 'r') as f:
#             grupos = json.load(f)
#     except FileNotFoundError:
#         grupo = {}

#     # Agregar el nuevo grupo
#     grupos[codigo] = grupo
#     print(f"Grupo {grupo['nombre']} fue registrado")

#     # Serializar el diccionario grupos a un string JSON
#     grupos_json = json.dumps(grupos, indent=4)

#     # Escribir el string JSON en el archivo dentro de la carpeta 'data'
#     with open(archivo_json, 'w') as f:
#         f.write(grupos_json)

# registro_grupo()




print('  ▄▀▀▀▀▄  ▄▀▀█▀▄   ▄▀▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄  ▄▀▀█▄  ')
print(' █ █   ▐ █   █  █ █ █   ▐ █        ▐  ▄▀   ▐ █ █   ▐ ▐ ▄▀ ▀▄ ')
print('    ▀▄   ▐   █  ▐    ▀▄   █    ▀▄▄   █▄▄▄▄▄     ▀▄     █▄▄▄█ ')
print(' ▀▄   █      █    ▀▄   █  █     █ █  █    ▌  ▀▄   █   ▄▀   █ ')
print('  █▀▀▀    ▄▀▀▀▀▀▄  █▀▀▀   ▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄    █▀▀▀   █   ▄▀  ')
print('  ▐      █       █ ▐      ▐         █    ▐    ▐      ▐   ▐  ') 
print('         ▐       ▐                  ▐                        ')