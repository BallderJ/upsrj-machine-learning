# Automatización: Organizador Inteligente de Descargas

En la carpeta de descargas es el lugar más desordenado de mi sistema. Al descargar archivos de todo tipo constantemente, se vuelve difícil localizarlos. Moverlos uno por uno es una tarea repetitiva y gasta tiempo.

He creado un script que centraliza todo el desorden en una única carpeta llamada **"Organizacion"**. Dentro de ella, el script crea subcarpetas automáticamente basadas en el tipo de archivo (PDF, IMAGENES, WORD, etc.) y mueve cada archivo a su lugar correspondiente.

## Algoritmo de la Solución
1. Localiza la ruta de Descargas del usuario en Ubuntu.
2. Verifica si existe la carpeta maestra llamada `Organizacion`; si no, la crea.
3. Lee todos los elementos de la carpeta de Descargas.
4. Para cada archivo encontrado:
    - Extrae su extensión.
    - Define un nombre de subcarpeta basado en esa extensión (ej: `.pdf` se convierte en la carpeta `PDF`).
    - Crea la subcarpeta dentro de `Organizacion` si no existe.
    - Mueve el archivo desde la raíz de Descargas hacia su nueva subcarpeta.
5. Ignora carpetas existentes para evitar errores de recursividad.

Una vez que tenga mis archivos ordenados en cada carpeta segun el tipo de archivo que es, es mas facil el buscar algun archivo necesario. 