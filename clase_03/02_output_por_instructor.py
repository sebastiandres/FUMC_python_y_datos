"""
Objetivo:
- Abrir el archivo excel, para la pestaña de Horarios (multiples convenciones posibles)
- Filtrar los horarios para un instructor en particular
- Guardar en un archivo excel:
    - Los horarios para un instructor en particular
    - Las secciones del instructor
    - El número de secciones por instructor
"""

# Importar la libreria pandas
import pandas as pd
import os

# Leer el archivo excel
filepath = os.path.join('input', 'raw', 'horarios.xlsx') # Ruta genérica para Linux, Mac y Windows

# Leer el archivo
sheet_names = pd.ExcelFile(filepath).sheet_names
demanda_name = ""
for sheet_name in sheet_names:
    all_names = sheet_name.split(" ")
    clean_name_1 = all_names[-1]
    clean_name_2 = clean_name_1.upper()
    if clean_name_2 == "HORARIOS":
        df = pd.read_excel(filepath, sheet_name=sheet_name)
        break

# Obtener la lista de todos los instructores
save_instructor_list = df["id_docente"].dropna().unique()
print(save_instructor_list)

# Crear una lista de (instructor, numero_secciones)
instructor_num_sections_list = []

for INSTRUCTOR_ID in save_instructor_list:
    print(INSTRUCTOR_ID)
    # Filtrar los horarios para un instructor en particular
    mask = df["id_docente"] == INSTRUCTOR_ID
    #print(mask)
    df_filtered = df[mask]
    print("(Filas, Columnas):", df_filtered.shape)
    print(df_filtered.head(5))

    # Secciones del instructor: Opcion 1 (Series de datos)
    output_cols = ["id_seccion"]
    df_section = df_filtered[output_cols].drop_duplicates()

    # Número de secciones por instructor
    num_sections = df_section.shape[0]
    print(num_sections, type(num_sections))
    df_num_sections = pd.DataFrame({"numero_secciones": [num_sections]})
    print(df_num_sections)

    # Guardar todos los outputs en un mismo archivo
    filename = f"horarios_instructor_{INSTRUCTOR_ID}.xlsx"
    output_filepath = os.path.join('output', filename)
    # Abrir el archivo excel para escribir
    excel_writer = pd.ExcelWriter(output_filepath, engine='xlsxwriter')
    # Escribir los horarios filtrados para el instructor
    df_filtered.to_excel(excel_writer, sheet_name="horarios_instructor", index=False)
    excel_writer.sheets["horarios_instructor"].autofit()
    # Escribir las secciones del instructor
    df_section.to_excel(excel_writer, sheet_name="secciones_instructor", index=False)
    excel_writer.sheets["secciones_instructor"].autofit()
    # Escribir el número de secciones por instructor
    df_num_sections.to_excel(excel_writer, sheet_name="numero_secciones", index=False)
    excel_writer.sheets["numero_secciones"].autofit()
    # Cerrar el archivo excel
    excel_writer.close()

    # Guardar en la lista de (instructor, numero_secciones)
    instructor_num_sections_list.append( (INSTRUCTOR_ID, num_sections))

print(instructor_num_sections_list)
# Convertir la lista a un dataframe
df_instructor_num_sections = pd.DataFrame(instructor_num_sections_list, 
                                            columns=["instructor_id", "numero_secciones"])
# Ordenar el dataframe por el número de secciones
df_instructor_num_sections = df_instructor_num_sections.sort_values(by="numero_secciones", ascending=False)
# Guardar en un archivo excel por separado
filename = "numero_secciones_instructores.xlsx"
output_filepath = os.path.join('output', filename)
excel_writer = pd.ExcelWriter(output_filepath, engine='xlsxwriter')
df_instructor_num_sections.to_excel(excel_writer, sheet_name="numero_secciones_instructores", index=False)
excel_writer.sheets["numero_secciones_instructores"].autofit()
excel_writer.close()