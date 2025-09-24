# Crear el diccionario con la información personal
informacion_personal = {
    "nombre": "Francis Muñoz",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

# Cambiar la ciudad (opcional)
informacion_personal["ciudad"] = "Quito"

# Agregar la clave "empresa"
informacion_personal["empresa"] = "Universidad UEA"

# Verificar si la clave "telefono" existe; si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998765432"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)

