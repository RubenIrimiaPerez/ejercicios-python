from datetime import datetime

# Solicita al usuario que ingrese una fecha en el formato YYYY-MM-DD
fecha_ingresada_str = input("Ingresa una fecha (YYYY-MM-DD): ")


# Convierte la cadena de fecha ingresada a un objeto datetime
fecha_ingresada = datetime.strptime(fecha_ingresada_str, "%Y-%m-%d")


# Obtiene la fecha y hora actuales
fecha_actual = datetime.now()

# Calcula la diferencia en días entre la fecha ingresada y la fecha actual
diferencia_en_dias = (fecha_actual - fecha_ingresada).days

# Muestra la diferencia en días
print(f"La diferencia en días entre {fecha_ingresada_str} y hoy es: {diferencia_en_dias} días.")
