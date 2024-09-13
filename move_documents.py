# Importa las librerias necesarias
import os
import shutil

# Obetener el path actual de donde voy a mover los archivos.
current_path = os.getcwd()

# Diccionario de destino para los archivos.
destination_path = {
    ".xlsx": r"C:\Users\leand\OneDrive - UNI\Escritorio\Excel",
    ".docx": r"C:\Users\leand\OneDrive - UNI\Escritorio\Word",
    ".pdf": r"C:\Users\leand\OneDrive - UNI\Escritorio\PDF"
}

# Listar todos los archivos que hay dentro del path.
archivos = os.listdir(current_path)

# Funcion para mover todos los archivos.
def move_documents(lista_de_archivos): 
    
    # Recorre todos los archivos dentro de la lista.
    for archivo in lista_de_archivos:

        # Extrae la extension de cada archivo de la lista.
        extension = os.path.splitext(archivo)[1]

        # Verifica si la extension esta dentro de las definidas en el diccionario.
        if extension in destination_path:

            try:
                # Mueve los archivos a la carpeta de destino
                shutil.move(os.path.join(current_path, archivo), destination_path[extension])
                print("Todo ha salido bien :)")

            # Imprime un error en caso de que lo haya
            except NameError as e:

                print(f"Ha ocurrido un error: {e.name}")
                

move_documents(archivos)


