import os
import shutil

# Obetener el path actual de donde voy a mover los archivos
current_path = os.getcwd()

# Paths de destino para los archivos
destiny_path_for_docx = r"C:\Users\leand\OneDrive - UNI\Escritorio\Word"
destiny_path_for_xlsx = r"C:\Users\leand\OneDrive - UNI\Escritorio\Excel" 
destiny_path_for_pdf = r"C:\Users\leand\OneDrive - UNI\Escritorio\PDF"

# Listar todos los archivos que hay dentro del path
archivos = os.listdir(current_path)

# Funcion para mover todos los archivos
def move_documents(lista_de_archivos): 

    # Recorrer todos los archivos buscando las extensiones: .xlsx | .docx | .pdf
    try:
        for archivo in lista_de_archivos:

            if archivo.endswith(".xlsx"):
                shutil.move(archivo, destiny_path_for_xlsx)
    
            if archivo.endswith(".pdf"):
                shutil.move(archivo, destiny_path_for_pdf)

            if archivo.endswith(".docx"):
                shutil.move(archivo, destiny_path_for_docx)

        print("Todo ha ido bien")
    
    except:
        pass

move_documents(archivos)
    

