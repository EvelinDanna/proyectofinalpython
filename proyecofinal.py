import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Programa para subir a repositorio")
ventana.geometry("500x300")  # Aumento el tamaño de la ventana

# Cambiar el color de fondo de la ventana
ventana.config(bg="lightblue")

# Etiqueta con texto y formato mejorado
etiqueta = tk.Label(
    ventana,
    text="Este programa es de Evelin y Danna",
    font=("Helvetica", 20, "bold"),  # Fuente más grande y en negrita
    fg="white",  # Color del texto
    bg="purple",  # Color de fondo de la etiqueta
    padx=20,  # Espaciado horizontal
    pady=20   # Espaciado vertical
)
etiqueta.pack(pady=30)  # Un poco más de espacio arriba y abajo de la etiqueta

# Mostrar la ventana
ventana.mainloop()
