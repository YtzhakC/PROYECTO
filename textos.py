from datetime import datetime, timedelta

# Hora de referencia (hora de llegada esperada)
hora_referencia = datetime.strptime('14:00', '%H:%M')

# Hora de llegada de la persona
hora_llegada = datetime.strptime('14:16', '%H:%M')
print(hora_llegada)
print(hora_referencia)
# Calcular la diferencia en minutos
diferencia = hora_llegada - hora_referencia

# Comprobar si la diferencia es mayor o igual a 15 minutos
if diferencia >= timedelta(minutes=15):
    print("La persona llegó 15 minutos después o más.")
else:
    print("La persona llegó antes de 15 minutos.")
