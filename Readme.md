# Script de Automatización: Organizador Inteligente y Analizador de Descargas

## 1. Planteamiento del Problema
En entornos de trabajo y estudio, la carpeta de "Descargas" suele ser un repositorio caótico de archivos. Este desorden no solo dificulta la búsqueda de información, sino que impide tener una visibilidad clara sobre el consumo de almacenamiento y el tipo de archivos que predominan en nuestro flujo de trabajo diario.

## 2. Propuesta de Solución
He desarrollado un script en Python que automatiza dos tareas principales:
1.  **Gestión de Archivos:** Organiza automáticamente los archivos de la carpeta de descargas de Windows (accediendo desde WSL/Ubuntu) hacia una carpeta centralizada llamada `Organizacion`, clasificándolos en subcarpetas según su extensión.
2.  **Análisis de Datos:** Utiliza las librerías **Pandas** y **Numpy** para recolectar metadatos de cada archivo movido (tamaño, categoría, fecha) y generar un reporte estadístico en formato CSV para su posterior análisis.

## 3. Algoritmo de la Solución
1.  **Localización:** Se identifica la ruta de Windows mediante el punto de montaje en WSL: `/mnt/c/Users/yo_of/Downloads`.
2.  **Preparación:** Se crea la carpeta maestra `Organizacion` si no existe.
3.  **Procesamiento:** Se itera sobre cada archivo en la carpeta de descargas:
    -   Se extrae la extensión y se define la categoría.
    -   **Cálculo con Numpy:** Se obtiene el tamaño del archivo y se convierte de Bytes a Megabytes (MB) con redondeo estadístico.
    -   **Movimiento:** Se traslada el archivo a su subcarpeta correspondiente.
4.  **Registro de Datos (Logging):** Los datos de cada archivo (nombre, categoría, tamaño en MB, fecha) se almacenan en una lista de diccionarios.
5.  **Análisis con Pandas:** 
    -   Se convierte la lista en un `DataFrame`.
    -   Se calculan estadísticas descriptivas (total de archivos, suma total de megabytes organizados).
    -   Se genera un conteo de frecuencia por categorías.
6.  **Exportación:** Se guarda el dataset resultante en un archivo `reporte_organizacion.csv`.

## 4. Herramientas Utilizadas
- **Python 3.x**
- **Pandas:** Para la creación del DataFrame y manipulación de la tabla de resultados.
- **Numpy:** Para el procesamiento numérico y cálculos de almacenamiento.
- **os & shutil:** Para la manipulación del sistema de archivos y movimiento de directorios.
- **Entorno:** Ejecutado en **Ubuntu (WSL)** accediendo al sistema de archivos de Windows.
