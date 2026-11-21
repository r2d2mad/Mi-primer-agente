empresas = [
    ("Talleres Garcia", 8),
    ("Logistica Toledo", 45),
    ("Industrias del Centro", 320),
    ("Ferreteria Local", 3),
]

for nombre, empleados in empresas:
    if empleados >= 100:
        prioridad = "ALTA"
    elif empleados >= 20:
        prioridad = "MEDIA"
    else:
        prioridad = "BAJA"
    print(nombre, "->", empleados, "empleados -> prioridad", prioridad)

print("Total de empresas revisadas:", len(empresas))
