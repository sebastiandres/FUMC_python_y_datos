"""
En este archivo se realiza la lectura de los datos contenidos en inputs/raw/
y se practica con el uso de listas y diccionarios.
"""

# Leer archivos
# Glob: permite usar regex (expresiones regulares) para encontrar archivos
import glob
import os

# Obtener la lista de archivos en el directorio inputs/raw/ (generico para cualquier OS)
regex_archivos = os.path.join("inputs", "raw", "*.txt")
print(regex_archivos)
mis_archivos = sorted(glob.glob(regex_archivos)) # * significa cualquier caracter
#print(mis_archivos)

# Leer cada archivo, y armar una lista de las personas
personas_list = []

# Procesamiento de nombres de personas para obtener una lista de nombres completos
for archivo in mis_archivos:
    # Leer el archivo
    with open(archivo, "r") as f:
        lines_list = f.readlines()
        linea_nombre = lines_list[0]
        nombre = linea_nombre.split(",")[0]
        apellido = linea_nombre.split(",")[1]
        apellido_clean = apellido.replace("\n", "").replace(" ", "")
        nombre_completo = f"{nombre} {apellido_clean}" # f-string para concatenar strings
        personas_list.append(nombre_completo)

# Procesamiento de peliculas
peliculas_dict = {}

for archivo in mis_archivos:
    # Leer el archivo
    with open(archivo, "r") as f:
        lines_list = f.readlines()
        pelicula = lines_list[1].strip()
        nombre_persona = lines_list[0].strip()
        nombre_persona = nombre_persona.replace(",", "").strip()        
        # Opcion 1:
        """
        if pelicula not in peliculas_dict:
            peliculas_dict[pelicula] = [nombre_persona, ]
        else:
            peliculas_dict[pelicula].append(nombre_persona)
        """
        # Opción 2:
        if pelicula not in peliculas_dict:
            peliculas_dict[pelicula] = []
        # Siempre
        peliculas_dict[pelicula].append(nombre_persona)

print(peliculas_dict)

# Tarea:
# Funciones a aprender y practicas: sorted, f-strings, listas (append, crear una lista vacia, iterar)
