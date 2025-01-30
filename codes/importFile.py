import tkinter as tk
from tkinter import filedialog

# Crear una ventana oculta
def get_path_of_image() -> str:
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    # Abrir el explorador de archivos y obtener la ruta del archivo seleccionado
    file_path = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")]
    )
    
    root.destroy()

    return file_path
