# temperaturas_promedio.py

# Función para calcular promedios de temperaturas de varias ciudades y semanas
def calcular_temperaturas_promedio(temperaturas, nombres_ciudades):
    """
    Calcula el promedio de temperatura de cada ciudad y determina
    la semana con mayor y menor promedio.

    Parámetros:
    temperaturas: list
        Lista 3D donde temperaturas[ciudad][semana][dia] contiene
        las temperaturas de cada día.
    nombres_ciudades: list
        Lista con los nombres de las ciudades correspondientes.

    Retorna:
    dict
        Diccionario con:
        - 'promedios': promedios por ciudad y semana
        - 'mayor': ciudad, semana y valor de la mayor temperatura promedio
        - 'menor': ciudad, semana y valor de la menor temperatura promedio
    """
    num_ciudades = len(temperaturas)
    num_semanas = len(temperaturas[0])
    num_dias = len(temperaturas[0][0])

    # Variables para resultados
    mayor_promedio = float('-inf')
    menor_promedio = float('inf')
    semana_mayor = None
    semana_menor = None
    ciudad_mayor = None
    ciudad_menor = None

    # Diccionario para guardar promedios
    promedios = {}

    for i in range(num_ciudades):
        promedios_ciudad = []
        for semana in range(num_semanas):
            promedio = sum(temperaturas[i][semana]) / num_dias
            promedios_ciudad.append(promedio)

            # Revisar mayor y menor promedio
            if promedio > mayor_promedio:
                mayor_promedio = promedio
                semana_mayor = semana + 1
                ciudad_mayor = nombres_ciudades[i]
            if promedio < menor_promedio:
                menor_promedio = promedio
                semana_menor = semana + 1
                ciudad_menor = nombres_ciudades[i]

        promedios[nombres_ciudades[i]] = promedios_ciudad

    resultados = {
        'promedios': promedios,
        'mayor': {'ciudad': ciudad_mayor, 'semana': semana_mayor, 'valor': mayor_promedio},
        'menor': {'ciudad': ciudad_menor, 'semana': semana_menor, 'valor': menor_promedio}
    }

    return resultados

# ----------------------
# Datos de ejemplo
temperaturas = [
    [   # Ibarra
        [22, 23, 21, 20, 24, 25, 23],
        [21, 22, 23, 24, 22, 21, 20]
    ],
    [   # Quito
        [18, 19, 20, 21, 19, 18, 20],
        [20, 21, 22, 23, 21, 20, 19]
    ],
    [   # Guayaquil
        [25, 26, 24, 23, 27, 28, 26],
        [24, 25, 26, 27, 25, 24, 23]
    ]
]

ciudades = ["Ibarra", "Quito", "Guayaquil"]

# ----------------------
# Ejecutar función
resultados = calcular_temperaturas_promedio(temperaturas, ciudades)

# Mostrar resultados
for ciudad, promedios in resultados['promedios'].items():
    print(f"\nCiudad {ciudad}:")
    for i, promedio in enumerate(promedios):
        print(f"  Semana {i+1}: Promedio de temperatura = {promedio:.2f} °C")

print("\n--------------------------------")
print(f"La semana con mayor temperatura fue la Semana {resultados['mayor']['semana']} en {resultados['mayor']['ciudad']} con {resultados['mayor']['valor']:.2f} °C")
print(f"La semana con menor temperatura fue la Semana {resultados['menor']['semana']} en {resultados['menor']['ciudad']} con {resultados['menor']['valor']:.2f} °C")

