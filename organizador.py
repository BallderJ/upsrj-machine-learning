import os
import shutil
import pandas as pd
import numpy as np
from datetime import datetime

def organizar_con_analisis():
    # Ruta para tu WSL
    ruta_descargas = "/mnt/c/Users/yo_of/Downloads"
    if not os.path.exists(ruta_descargas):
        ruta_descargas = "/mnt/c/Users/yo_of/Descargas"

    carpeta_maestra = os.path.join(ruta_descargas, "Organizacion")
    if not os.path.exists(carpeta_maestra):
        os.makedirs(carpeta_maestra)

    # Lista para recolectar datos para nuestro DataFrame
    datos_archivos = []

    print(f"--- Analizando y Organizando ---")

    for archivo in os.listdir(ruta_descargas):
        ruta_origen = os.path.join(ruta_descargas, archivo)

        if os.path.isfile(ruta_origen):
            nombre, extension = os.path.splitext(archivo)
            if not extension: continue

            # Obtener peso del archivo en bytes usando os
            peso_bytes = os.path.getsize(ruta_origen)
            # USAMOS NUMPY: Convertir a Megabytes y redondear
            peso_mb = np.round(peso_bytes / (1024 * 1024), 2)

            categoria = extension.replace(".", "").upper()
            
            # Clasificación personalizada
            if categoria in ["JPG", "PNG", "GIF"]: categoria = "IMAGENES"
            elif categoria in ["PDF"]: categoria = "DOCUMENTOS_PDF"

            ruta_destino_folder = os.path.join(carpeta_maestra, categoria)
            if not os.path.exists(ruta_destino_folder):
                os.makedirs(ruta_destino_folder)

            # Mover archivo
            shutil.move(ruta_origen, os.path.join(ruta_destino_folder, archivo))

            # GUARDAR DATOS PARA EL ANÁLISIS
            datos_archivos.append({
                "Nombre": archivo,
                "Extension": extension.lower(),
                "Categoria": categoria,
                "Tamaño_MB": peso_mb,
                "Fecha_Procesado": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    # --- USO DE PANDAS ---
    if datos_archivos:
        df = pd.DataFrame(datos_archivos)
        
        # Guardar el registro en un CSV dentro de la carpeta Organizacion
        ruta_reporte = os.path.join(carpeta_maestra, "reporte_organizacion.csv")
        df.to_csv(ruta_reporte, index=False)

        # MOSTRAR ESTADÍSTICAS EN CONSOLA USANDO PANDAS Y NUMPY
        print("\n" + "="*30)
        print("RESUMEN DE OPERACIÓN (Pandas)")
        print("="*30)
        print(f"Total de archivos movidos: {len(df)}")
        print(f"Espacio total organizado: {np.sum(df['Tamaño_MB'])} MB")
        print("\nConteo por categoría:")
        print(df['Categoria'].value_counts())
        print(f"\nReporte guardado en: {ruta_reporte}")
    else:
        print("No había archivos nuevos para organizar.")

if __name__ == "__main__":
    organizar_con_analisis()
#codigo