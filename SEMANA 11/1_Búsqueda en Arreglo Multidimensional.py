# Programa 1: Búsqueda en Arreglo Multidimensional

# Definir la matriz 3x3
matriz = [
    [3, 8, 5],
    [1, 9, 7],
    [4, 6, 2]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # devolver posición (fila, columna)
    return None

# Valor que quieres buscar
valor_a_buscar = 7

print("Matriz:")
for fila in matriz:
    print(fila)

# Llamar a la función
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostrar resultado
if posicion:
    print(f"\n✅ El valor {valor_a_buscar} se encontró en la posición: fila {posicion[0]}, columna {posicion[1]}")
else:
    print(f"\n❌ El valor {valor_a_buscar} no se encontró en la matriz.")
