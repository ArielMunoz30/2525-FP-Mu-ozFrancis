# Datos: 3 ciudades, 2 semanas, 7 días cada semana
# temperaturas[ciudad][semana][dia]
temperaturas = [
    [   # Ciudad 0
        [22, 23, 21, 20, 24, 25, 23],   # Semana 1
        [21, 22, 23, 24, 22, 21, 20]    # Semana 2
    ],
    [   # Ciudad 1
        [18, 19, 20, 21, 19, 18, 20],   # Semana 1
        [20, 21, 22, 23, 21, 20, 19]    # Semana 2
    ],
    [   # Ciudad 2
        [25, 26, 24, 23, 27, 28, 26],   # Semana 1
        [24, 25, 26, 27, 25, 24, 23]    # Semana 2
    ]
]

num_ciudades = len(temperaturas)
num_semanas = len(temperaturas[0])
num_dias = len(temperaturas[0][0])

# Variables para guardar la semana con mayor y menor promedio
mayor_promedio = float('-inf')
menor_promedio = float('inf')
semana_mayor = None
semana_menor = None
ciudad_mayor = None
ciudad_menor = None

# Promedios
for ciudad in range(num_ciudades):
    print(f"\nCiudad {ciudad}:")
    for semana in range(num_semanas):
        suma = 0
        for dia in range(num_dias):
            suma += temperaturas[ciudad][semana][dia]
        promedio = suma / num_dias
        print(f"  Semana {semana+1}: Promedio de temperatura = {promedio:.2f} °C")

        # Comparar para encontrar mayor y menor
        if promedio > mayor_promedio:
            mayor_promedio = promedio
            semana_mayor = semana + 1
            ciudad_mayor = ciudad
        if promedio < menor_promedio:
            menor_promedio = promedio
            semana_menor = semana + 1
            ciudad_menor = ciudad

# Resultados
print("\n--------------------------------")
print(f"La semana con mayor temperatura fue la Semana {semana_mayor} en la Ciudad {ciudad_mayor} con {mayor_promedio:.2f} °C")
print(f"La semana con menor temperatura fue la Semana {semana_menor} en la Ciudad {ciudad_menor} con {menor_promedio:.2f} °C")
