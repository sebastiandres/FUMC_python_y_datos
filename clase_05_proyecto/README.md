## Desafío: Procesamiento y Limpieza de Datos

### Contexto
En este desafío, los estudiantes deberán generar uno o más scripts para procesar y limpiar datos de tres tipos de archivos: un archivo Excel, un archivo CSV y un archivo Parquet. Cada uno de estos archivos contiene información sobre instructores, pero con diferentes columnas y datos adicionales. El objetivo es enseñar a los estudiantes sobre la limpieza y el procesamiento de datos.

### Entregable
- Un archivo README.md que explique el proceso que seguiste para generar y limpiar los datos, así como cualquier desafío que encontraste y cómo lo resolviste.
- Archivos .py que generen los datos y realicen el procesamiento y limpieza de los datos.
- Un archivo requirements.txt que contenga las librerías necesarias para ejecutar los archivos .py.
- Un archivo .xlsx único que contenga 2 columnas: 'identificador_docente' y 'nombre_docente'. Estas 2 columnas deben contener los datos de los archivos originales, pero sin duplicados ni datos nulos. La cantidad de filas del archivo .xlsx debe ser la misma que la cantidad de valores distintos en la columna 'identificador_docente'.

Los archivos solicitados deben estar en un repositorio de GitHub. El archivo .py debe poder ejecutarse en un entorno de Python sin errores, con las librerías del requirements.txt, y los archivos .xlsx deben poder abrirse en Excel.

### Pasos sugeridos
1. Procesar el archivo Excel, y generar un archivo con las 2 columnas mencionadas.
2. Procesar el archivo CSV, y generar un archivo con las 2 columnas mencionadas.
3. Procesar el archivo Parquet, y generar un archivo con las 2 columnas mencionadas.
4. Abrir los 3 archivos generados en el paso anterior en uno solo.
