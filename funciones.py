from datetime import datetime
from tkinter import ttk
from tkinter import *




#funcion para centrar la ventana
def centrar_ventana(ventana,ancho_ventana,alto_ventana):
    # Obtener el tamaño de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    # Establecer el tamaño y la posición de la ventana
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    
# Función para actualizar la hora y la fecha
def actualizar_hora(fecha_label,hora_label):
    # Obtener la fecha y hora actual
    ahora = datetime.now()
    fecha_actual = ahora.strftime("%d/%m/%Y")  # Formato de fecha
    hora_actual = ahora.strftime("%I:%M %p")    # Formato de hora en 12 horas con AM/PM

    # Actualizar las etiquetas
    fecha_label.config(text=fecha_actual)
    hora_label.config(text=hora_actual)

    # Programar la actualización cada segundo
    hora_label.after(1000, actualizar_hora, fecha_label, hora_label)
    

# funcion para salir
def salir_aplicacion(ventana):
    ventana.destroy()  

#funcion para convertir la primera letra en mayuscula    
def mayuscula_primera_letra(entry):
    
    def callback(evento):
        texto = entry.get()
        palabras = texto.split()
        palabras_mayusculas = [palabra.capitalize() for palabra in palabras]
        entry.delete(0, END)
        entry.insert(0, ' '.join(palabras_mayusculas))
    return callback     
    
    
    

  
    