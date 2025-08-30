# Programa 2: Ordenación de Arreglo Multidimensional (Bubble Sort en una fila específica)

# Definir la matriz 3x3
matriz = [
    [3, 8, 5],
    [9, 1, 7],
    [4, 6, 2]
]

# Función Bubble Sort para ordenar una lista
def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila):
    matriz[fila] = bubble_sort(matriz[fila])
    return matriz

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (ejemplo: fila 1 → segunda fila)
fila_a_ordenar = 1
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostrar matriz con la fila ordenada
print(f"\nMatriz después de ordenar la fila {fila_a_ordenar}:")
for fila in matriz_ordenada:
    print(fila)
