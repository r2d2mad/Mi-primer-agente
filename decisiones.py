empresa = input("Nombre de la empresa: ")
empleados = int(input("¿Cuántos empleados tiene? "))

if empleados >= 100:
    print(empresa, "es una cuenta GRANDE: prioridad alta.")
elif empleados >= 20:
    print(empresa, "es una cuenta MEDIANA: prioridad media.")
else:
    print(empresa, "es una cuenta PEQUEÑA: prioridad baja.")
