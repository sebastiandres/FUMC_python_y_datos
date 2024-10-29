# Lectura de un archivo excel
# Nombre del archivo: input/raw/horarios.xlsx

# Importar la libreria pandas
import pandas as pd
import os

# Leer el archivo excel
filepath = os.path.join('input', 'raw', 'horarios.xlsx') # Ruta genérica para Linux, Mac y Windows

# Objetivo: Mostrar las primeras 5 filas de la hoja "I1 Demanda"

# 1. Obtener las hojas que vienen en el archivo excel
sheet_names = pd.ExcelFile(filepath).sheet_names
#print(sheet_names)

# 2. Crear un nombre simplificado para cada hoja
demanda_name = ""
for sheet_name in sheet_names:
    print("-"*50)
    print(f"Sheet name: {sheet_name}")
    # Separar el nombre de la hoja usando como separador un espacio
    all_names = sheet_name.split(" ")
    print(all_names)
    # Tomar el último nombre
    clean_name_1 = all_names[-1]
    print(clean_name_1)
    # Pasar todo a mayusculas
    clean_name_2 = clean_name_1.upper()
    print(clean_name_2)
    # Abrir la hoja con la demanda
    if clean_name_2 == "DEMANDA":
        df = pd.read_excel(filepath, sheet_name=sheet_name)
        break

# 3. Mostrar las primeras 5 filas de la hoja con la demanda
print(df.head(5))
