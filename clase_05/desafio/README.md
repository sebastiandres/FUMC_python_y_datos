## Desafío: Procesamiento y Limpieza de Datos

El rector de la universidad APLAPLAC quiere organizar una fiesta para todos los docentes que han trabajado en la universidad en los últimos años. Sin embargo, no tiene una lista de los docentes puesto que la información se encuentra dispersa en distintos sistemas de la universidad. 

Para poder organizar la fiesta, el rector necesita conocer un archivo excel con 2 columnas:  el identificador del docente y el nombre del docente, de manera de poder enviarles las invitaciones mediante el sistema de correo electrónico de la universidad. 

Debido a tu conocimiento de python y datos, el rector personalmente te ha pedido que generes el archivo excel con la información necesaria para la fiesta.

Existen 3 archivos que contienen información sobre los docentes de la universidad:

- `docentes_1.xlsx`: contiene información sobre los instructores de la universidad y la secciones que dictaron. Este archivo fue generado manualmente por distintas personas antes de que la universidad creara un sistema para la gestión de docentes. Por lo tanto, puede contener errores. Tiene las columnas ID_SECCION, ID_DOCENTE, NOMBRE_DOCENTE, FECHA_NACIMIENTO.
- `docentes_2.csv`: contiene información sobre los instructores de la universidad y la cantidad de secciones que dictaron. Este archivo fue generado automáticamente por un sistema de la universidad, por lo que no debiera contener errores. Tiene las columnas id_docente, nombre_docente, dirección, numero_secciones
- `docentes_3.parquet`: contiene información sobre los periodos académicos en los que trabajó un instructor y el tipo de contrato que tenía. Este archivo fue generado automáticamente por un sistema de la universidad, por lo que no debiera contener errores. Tiene las columnas idDocente, nombreDocente, contrato, periodoAcademico

### Enlaces
Repositorio de GitHub: https://github.com/sebastiandres/FUMC_python_y_datos
Directorio: clase_05/desafio

### Entregables
Para resolver este desafío, debes entregar:
- Un archivo README.md que explique el proceso que seguiste para generar y limpiar los datos, así como cualquier dificultad que encontraste y cómo lo resolviste.
- Archivos .py que realicen el procesamiento y limpieza de los datos.
- Un archivo requirements.txt que contenga las librerías necesarias para ejecutar los archivos .py.
- Un archivo .xlsx único que contenga 2 columnas: 'identificador_docente' y 'nombre_docente'. Estas 2 columnas deben contener los datos de los archivos originales, pero sin duplicados ni datos nulos. La cantidad de filas del archivo .xlsx debe ser la misma que la cantidad de valores distintos en la columna 'identificador_docente'.

Los archivos solicitados deben estar en un repositorio de GitHub. El archivo .py debe poder ejecutarse en un entorno de Python sin errores, con las librerías del requirements.txt, y los archivos .xlsx deben poder abrirse en Excel.

### Pasos sugeridos
1. Procesar el archivo Excel, y generar un archivo con las 2 columnas mencionadas.
2. Procesar el archivo CSV, y generar un archivo con las 2 columnas mencionadas.
3. Procesar el archivo Parquet, y generar un archivo con las 2 columnas mencionadas.
4. Abrir los 3 archivos generados en el paso anterior en uno solo.
