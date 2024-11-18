import pandas as pd
import os

# Leer el archivo excel
input_filepath = os.path.join('input', 'clean', 'Horarios.xlsx')
input_df = pd.read_excel(input_filepath).fillna('')    # Reemplazar NaN por '' para saber si hay duplicados y poder contar correctamente

# Abrir un archivo de excel para guardar los resultados
output_filepath = os.path.join('output', 'Analisis_Horarios.xlsx')
excel_writer = pd.ExcelWriter(output_filepath, engine='openpyxl')

# Imprimir las columnas del archivo
print(input_df.columns)

# Obtener relación unica para bloque, y saber si hay duplicados
cols = ["BLOQUE", "CAPACIDAD_BLOQUE"]
bloque_df = input_df[cols].drop_duplicates() # Obtener relación unica para BLOQUE-CAPACIDAD_BLOQUE
# Verificar si hay duplicados
mask = bloque_df.duplicated(subset=['BLOQUE'], keep=False)
bloques_duplicados = bloque_df[mask]
if bloques_duplicados.empty:
    print("No hay bloques duplicados")
else:
    print("Hay bloques duplicados")
    print(bloques_duplicados)
bloque_df.to_excel(excel_writer, sheet_name='Bloques', index=False)

# Obtener relación única para el curso
cols = ["MATERIA", "CURSO", "DESCRIPCIÓN_CURSO", "TAXONOMIA_CURSO"]
curso_df = input_df[cols].drop_duplicates() # Obtener relación unica para MATERIA-CURSO-DESCRIPCIÓN_CURSO-TAXONOMIA_CURSO
curso_df["ID_CURSO"] = curso_df["MATERIA"] + curso_df["CURSO"].astype(str)
# Verificar si hay duplicados
mask = curso_df.duplicated(subset=['ID_CURSO'], keep=False)
cursos_duplicados = curso_df[mask]
if cursos_duplicados.empty:
    print("No hay cursos duplicados")
else:
    print("Hay cursos duplicados")
    print(cursos_duplicados)
output_curso_df = curso_df[["ID_CURSO", "MATERIA", "CURSO", "TAXONOMIA_CURSO", "DESCRIPCIÓN_CURSO"]]
output_curso_df.to_excel(excel_writer, sheet_name='Cursos', index=False)

# Estimar capacidad de salón, usando las columnas: EDIFICIO, SALON, INSCRITOS
## 1. Crear identificador único de salón, concatenando EDIFICIO y SALON
## 2. Convertir la columna INSCRITOS a un número entero
## 3. Estimar la capacidad de cada salón (por identificador único), considerando el máximo de los INSCRITOS
input_df["ID_SALON"] = input_df["EDIFICIO"].astype(str) + "-" + input_df["SALON"].astype(str)
input_df["INSCRITOS"] = input_df["INSCRITOS"].astype(int)
capacidad_salon_df = input_df[["ID_SALON", "INSCRITOS"]].groupby("ID_SALON").max().reset_index()
capacidad_salon_df.to_excel(excel_writer, sheet_name='Capacidad_Salones', index=False)

# Cerrar el archivo de excel
excel_writer.close()
