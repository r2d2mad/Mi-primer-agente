def calcular_prioridad(empleados):
    if empleados >= 100:
        return "ALTA"
    elif empleados >= 20:
        return "MEDIA"
    else:
        return "BAJA"


def redactar_mensaje(nombre, prioridad):
    if prioridad == "ALTA":
        return "Hola, " + nombre + ". Me gustaría presentarle una propuesta de suministro industrial a medida. ¿Tiene 15 minutos esta semana?"
    elif prioridad == "MEDIA":
        return "Hola, " + nombre + ". Le escribo para ofrecerle condiciones ventajosas en suministro industrial. ¿Le envío información?"
    else:
        return "Hola, " + nombre + ". Pasaré por la zona y me gustaría dejarle nuestro catálogo."


empresas = [
    ("Talleres Garcia", 8),
    ("Logistica Toledo", 45),
    ("Industrias del Centro", 320),
]

for nombre, empleados in empresas:
    prioridad = calcular_prioridad(empleados)
    mensaje = redactar_mensaje(nombre, prioridad)
    print(nombre, "->", prioridad)
    print(mensaje)
    print()
