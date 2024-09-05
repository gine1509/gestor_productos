from tkinter import *
from funciones import *
from tkinter import messagebox

def inicio_sesion():
    login_exitoso = False  

    def verificar_usuario():
        nonlocal login_exitoso  
        usuario_ingresado = usuario.get()
        contraseña_ingresada = contraseña.get()
        
        usuario_esperado = "admin"
        contraseña_esperada = "12345"
        
        if usuario_ingresado == usuario_esperado and contraseña_ingresada == contraseña_esperada:
            messagebox.showinfo("Inicio de Sesión", "Bienvenido")
            login_exitoso = True  
            ventana.destroy()  
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    
    ventana = Tk()
    ventana.title("Login Gestor de Productos")
    ventana.resizable(width=0, height=0)
    ventana.config(bg="#e5e4fb")
    centrar_ventana(ventana, 450, 300)

    
    frame_form = Frame(ventana, bd=0, relief=SOLID)
    frame_form.pack(side=RIGHT, expand=YES, fill=BOTH)

    
    frame_inicio_sesion = Frame(frame_form, height=30, bd=0, relief=SOLID)
    frame_inicio_sesion.pack(side=TOP, fill=X)
    titulo = Label(frame_inicio_sesion, text="Inicio de Sesión", font=("arial", 22), fg="black", pady=10)
    titulo.pack(expand=YES, fill=BOTH)

    
    otro_frame = Frame(frame_form, height=50, relief=SOLID, bd=0)
    otro_frame.pack(side=BOTTOM, expand=YES, fill=BOTH)
    etiqueta_usuario = Label(otro_frame, text="Usuario", font=("arial", 14), fg="black", anchor=W)
    etiqueta_usuario.pack(fill=X, padx=20, pady=5)
    usuario = Entry(otro_frame, font=("arial", 12))
    usuario.pack(fill=X, padx=20, pady=10)
    etiqueta_contraseña = Label(otro_frame, text="Contraseña", font=("arial", 14), fg="black", anchor=W)
    etiqueta_contraseña.pack(fill=X, padx=20, pady=5)
    contraseña = Entry(otro_frame, font=("arial", 12))
    contraseña.pack(fill=X, padx=20, pady=10)
    contraseña.config(show="*")

    
    boton = Button(otro_frame, text="Iniciar Sesión", font=("arial", 15, "bold"), bg="RoyalBlue3", bd=0, fg="white", cursor="hand2", command=lambda: verificar_usuario())
    boton.pack(fill=X, padx=20, pady=20)

    ventana.mainloop()

    
    return login_exitoso