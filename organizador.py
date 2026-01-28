import os
import shutil

def organizar_descargas():
    # 1. Detectar la carpeta de descargas en Ubuntu
    home = os.path.expanduser("~")
    nombres_posibles = ["Downloads", "Descargas"]
    ruta_descargas = "/mnt/c/Users/yo_of/Downloads"

    for nombre in nombres_posibles:
        if os.path.exists(os.path.join(home, nombre)):
            ruta_descargas = os.path.join(home, nombre)
            break

    if not ruta_descargas:
        print("No se encontró la carpeta de descargas.")
        return

    # 2. Definir la Carpeta Principal de Organización
    carpeta_maestra = os.path.join(ruta_descargas, "Organizacion")
    
    if not os.path.exists(carpeta_maestra):
        os.makedirs(carpeta_maestra)
        print(f"Carpeta creada: {carpeta_maestra}")

    print(f"--- Organizando archivos en: {carpeta_maestra} ---")

    # 3. Recorrer los archivos
    for archivo in os.listdir(ruta_descargas):
        ruta_completa_archivo = os.path.join(ruta_descargas, archivo)

        # Solo procesar archivos (ignorar la propia carpeta 'Organizacion' y otras carpetas)
        if os.path.isfile(ruta_completa_archivo):
            nombre, extension = os.path.splitext(archivo)
            
            # Si el archivo no tiene extensión, lo saltamos
            if not extension:
                continue
            
            # Limpiar la extensión para el nombre de la carpeta (ej: .pdf -> PDF)
            nombre_carpeta = extension.replace(".", "").upper()
            
            # Casos especiales: agrupar formatos similares si quieres
            if nombre_carpeta in ["JPG", "JPEG", "PNG", "GIF", "SVG"]:
                nombre_carpeta = "IMAGENES"
            elif nombre_carpeta in ["DOC", "DOCX"]:
                nombre_carpeta = "WORD"
            elif nombre_carpeta in ["XLS", "XLSX"]:
                nombre_carpeta = "EXCEL"

            # 4. Crear la subcarpeta dentro de 'Organizacion'
            ruta_subcarpeta = os.path.join(carpeta_maestra, nombre_carpeta)
            if not os.path.exists(ruta_subcarpeta):
                os.makedirs(ruta_subcarpeta)

            # 5. Mover el archivo
            try:
                shutil.move(ruta_completa_archivo, os.path.join(ruta_subcarpeta, archivo))
                print(f"[OK] {archivo} -> Organizacion/{nombre_carpeta}/")
            except Exception as e:
                print(f"[ERROR] No se pudo mover {archivo}: {e}")

    print("\n¡Limpieza completada con éxito!")

if __name__ == "__main__":
    organizar_descargas()