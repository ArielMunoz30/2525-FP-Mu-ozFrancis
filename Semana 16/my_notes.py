
# Descripción: Este programa crea un archivo de texto, escribe notas personales,
#              luego lo lee línea por línea y finalmente cierra el archivo.
# Cree un archivo llamado "my_notes.txt"
with open("my_notes.txt", "w") as file:
    # Notas personales
    file.write("Nota 1: Hoy estuve trabajando y estudiando lo aprendido en clases.\n")
    file.write("Nota 2: Apredi que el metodo write() me permite escribir en un archivo.\n")
    file.write("Nota 3: Y tambien que puedo leer línea por línea usando readline. Interesante -_-().\n")
# El bloque 'with' cierra automáticamente el archivo al terminar.
# 2. Lectura de Archivo de Texto
# Abri el archivo en modo lectura
file = open("my_notes.txt", "r")
print("Contenido del archivo línea por línea:\n")
# Use readline() dentro de un bucle para leer línea por línea
linea = file.readline()   # Lee la primera línea
while linea:
    print(linea.strip())  # strip() elimina saltos de línea extra al imprimir
    linea = file.readline()  # Lee la siguiente línea
# 3. Cierre de Archivo
file.close()  # Se cierra el archivo manualmente
print("\nArchivo cerrado correctamente.")
#Fin -_-