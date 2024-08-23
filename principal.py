from tkinter import *
from datetime import datetime
from tkinter import messagebox
from tkinter import ttk
from funciones import *
from conexion import *

ventana = Tk()
ventana.title("Gestor de Productos")
ventana.resizable(width=0, height=0)
ventana.config(bg="#e5e4fb")
centrar_ventana(ventana,1000, 550)

from iconos import *


# icono
ventana.iconphoto(False, principal)

# header
encabezado = Frame(ventana, bg="RoyalBlue3", height=65)
encabezado.pack(side=TOP, fill="both")

# icono encabezado
icono_encabezado = Label(encabezado, image=encabezado_icono, bg="RoyalBlue3")
icono_encabezado.pack(side=LEFT, padx=(10, 0),pady=5)

# etiqueta producto
palabra_producto = Label(encabezado, text="Gestor de Productos")
palabra_producto.config(fg="white", font=("arial black", 20), bg="RoyalBlue3", pady=10)
palabra_producto.pack(side=LEFT)


#etiqueta de la fecha
fecha_label = Label(encabezado,image=fecha, compound=LEFT, font=("Arial", 12,"bold"), fg="white", bg="RoyalBlue3")
fecha_label.pack(side=RIGHT, padx=(5, 10), pady=10)

#etiqueta de la hora    
hora_label = Label(encabezado,image=hora, compound=LEFT, font=("Arial", 12,"bold"), fg="white", bg="RoyalBlue3")
hora_label.pack(side=RIGHT, padx=(5, 10), pady=10)

# Inicializar la hora
actualizar_hora(fecha_label,hora_label)

# funcion para abrir el formulario de agregar cliente
def abrir_ventana_agregar_producto():
        ventana_agregar = Toplevel(ventana)
        ventana_agregar.title("Agregar Producto")
        ventana_agregar.resizable(width=0, height=0)
        ventana_agregar.config(bg="#e5e4fb")
        centrar_ventana(ventana_agregar,480, 370)

        ventana_agregar.iconphoto(True, icono_ventana)
        
        # contenedor del formulario----------------------------------------
        con_formulario = LabelFrame(ventana_agregar, text="Agregar Nuevo Producto",fg="RoyalBlue3", font=("arial", 20, "bold"), bg="#e5e4fb")
        con_formulario.pack(side=LEFT, fill=BOTH, expand=True,padx=20, pady=20)

        # codigo de producto-------------------------------
        codigo = Label(con_formulario, text="ID del producto:",font=("arial",12), bg="#e5e4fb")
        codigo.grid(row=0, column=0, padx=5, pady=10)

        # nombre del producto-----------------------------------
        producto = Label(con_formulario, text="Nombre del Producto:",font=("arial",12), bg="#e5e4fb")
        producto.grid(row=1, column=0, padx=5, pady=10)
        entrada_producto = Entry(con_formulario, width=20, font=("arial", 12))
        entrada_producto.bind("<KeyRelease>", mayuscula_primera_letra(entrada_producto))
        entrada_producto.focus()
        entrada_producto.grid(row=1, column=1, padx=5, pady=5)

        # precio -------------------------------------------------------------
        precio_venta = Label(con_formulario, text="Precio del Producto:", font=("arial",12), bg="#e5e4fb")
        precio_venta.grid(row=3, column=0, padx=5, pady=10)
        entrada_precio = Entry(con_formulario, width=7, font=("arial", 12))
        entrada_precio.grid(row=3, column=1, sticky="W", padx=(0, 5), pady=2)

        # cantidad --------------------------------------------------
        cantidad = Label(con_formulario, text="Cantidad Inicial:",font=("arial",12), bg="#e5e4fb")
        cantidad.grid(row=4, column=0, padx=(0, 5), pady=10)
        entrada_cantidad = Entry(con_formulario, width=7, font=("arial", 12))
        entrada_cantidad.grid(row=4, column=1, sticky="W", padx=(0, 5), pady=2)

        # categoria-------------------------------------------------------------
        categoria = Label(con_formulario, text="Categoría del Producto:",font=("arial",12), bg="#e5e4fb")
        categoria.grid(row=5, column=0, padx=0, pady=10)
        menu = ttk.Combobox(con_formulario, values=["", "Opción 1", "Opción 2", "Opción 3", "Opción 4"], font=("arial", 12))
        menu.set("Seleccione")
        menu.config(state="readonly")
        menu.config(width=12)
        menu.grid(row=5, column=1, sticky="W", padx=(0, 5), pady=5)
        
        def abrir_categoria():
            ventana_categoria = Toplevel(ventana_agregar)
            ventana_categoria.title("Agregar Categoría")
            ventana_categoria.resizable(width=0, height=0)
            ventana_categoria.config(bg="#e5e4fb")
            centrar_ventana(ventana_categoria, 480, 370)

            # Formulario
            con_formulario_categoria = LabelFrame(ventana_categoria, text="Agregar Nueva Categoría", fg="RoyalBlue3", font=("arial", 14, "bold"), bg="#e5e4fb")
            con_formulario_categoria.place(x=100, y=10)

            categoria_label = Label(con_formulario_categoria, text="Nombre de la Categoría:", font=("arial", 10), bg="#e5e4fb")
            categoria_label.grid(row=0, column=0, padx=5, pady=10)

            entrada_categoria = Entry(con_formulario_categoria, width=15, font=("arial", 10))
            entrada_categoria.bind("<KeyRelease>", mayuscula_primera_letra(entrada_categoria))
            entrada_categoria.focus()
            entrada_categoria.grid(row=0, column=1, padx=5, pady=5)

            boton_guardar_categoria = Button(con_formulario_categoria, text="Guardar Categoría", font=("arial", 10, "bold"), fg="white", bg="RoyalBlue3", cursor="hand2", width=10)
            boton_guardar_categoria.grid(row=1, column=0,sticky="ew", padx=10, pady=5)

            boton_cancelar_categoria = Button(con_formulario_categoria, text="Cancelar", font=("arial", 10, "bold"), fg="white", bg="gray30", cursor="hand2", width=10)
            boton_cancelar_categoria.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

            # Buscar categorías
            buscar_categoria_label = Label(ventana_categoria, text="Buscar Categoría:", font=("arial", 10), bg="#e5e4fb")
            buscar_categoria_label.place(x=125,y=143)

            buscar_categoria_entry = Entry(ventana_categoria, width=20, font=("arial", 10))
            buscar_categoria_entry.bind("<KeyRelease>", mayuscula_primera_letra(buscar_categoria_entry))
            buscar_categoria_entry.place(x=245,y=145)

            buscar_categoria_boton = Button(ventana_categoria, image=buscar_cat,compound=RIGHT,text="Buscar", font=("arial", 10, "bold"), fg="white", bg="RoyalBlue3", cursor="hand2", width=65)
            buscar_categoria_boton.image=buscar_cat
            buscar_categoria_boton.place(x=400,y=141)

            # Contenedor para la tabla
            frame_contenedor = Frame(ventana_categoria, bg="#e5e4fb")
            frame_contenedor.place(x=30,y=190)

            # Tabla de categorías   
            categorias_treeview = ttk.Treeview(frame_contenedor, columns=("id", "nombre"), show="headings",height=7)
            categorias_treeview.pack(side=LEFT, fill="both", expand=False)
            
            # Configurar los encabezados de la tabla
            categorias_treeview.heading("id", text="ID", anchor=CENTER)
            categorias_treeview.heading("nombre", text="Nombre", anchor=CENTER)

            # Ajustar el ancho de las columnas
            categorias_treeview.column("#0", width=55, stretch=False, anchor=CENTER)
            categorias_treeview.column("id", width=55, stretch=True, anchor=CENTER)
            categorias_treeview.column("nombre", width=140, stretch=True, anchor=CENTER)

            # Scrollbar
            vertical = ttk.Scrollbar(frame_contenedor, orient="vertical", command=categorias_treeview.yview)
            vertical.pack(side="right", fill=Y)
            categorias_treeview.config(yscrollcommand=vertical.set)

            # Botones de editar y eliminar
            editar_categoria_boton = Button(ventana_categoria,image=editar_cat, compound=RIGHT, text="Editar", font=("arial", 10, "bold"), fg="white", bg="RoyalBlue3", cursor="hand2", width=75)
            editar_categoria_boton.image=editar_cat
            editar_categoria_boton.place(x=255,y=280)

            eliminar_categoria_boton = Button(ventana_categoria,image=eliminar_cat,compound=RIGHT, text="Eliminar", font=("arial", 10, "bold"), fg="white", bg="RoyalBlue3", cursor="hand2", width=75)
            eliminar_categoria_boton.image=eliminar_cat
            eliminar_categoria_boton.place(x=255,y=320)

            # Salir
            boton_salir = Button(ventana_categoria, image=salir_cat, bg="#e5e4fb", relief="flat", cursor="hand2",command=lambda: salir_aplicacion(ventana_categoria))
            boton_salir.image = salir_cat
            boton_salir.place(x=5, y=5)

            
        
        #boton para agregar categoria
        cate=Button(con_formulario,image=categoria_icono,bg="#e5e4fb",relief="flat",cursor="hand2",command=lambda: abrir_categoria())
        cate.image=categoria_icono
        cate.place(x=370,y=183)

        # boton guardar producto---------------------------------------------------
        boton = Button(con_formulario, text="Guardar Producto", font=("arial", 12, "bold"), fg="white", bg="RoyalBlue3",width=20,cursor="hand2")
        boton.grid(row=6, column=0, sticky="ew",padx=10,pady=5)

        # Botón de "Cancelar"
        cancelar_button = Button(con_formulario, text="Cancelar", font=("arial", 12, "bold"), fg="white", bg="gray30",cursor="hand2")
        cancelar_button.grid(row=6, column=1, sticky="ew", padx=10,pady=5)  



# boton agregar Producto
boton_agregar_producto = Button(ventana, image=agregar, compound=LEFT,text="Agregar Producto",background="RoyalBlue3", foreground="white", font=("Arial", 14, "bold"),cursor="hand2",padx=10, pady=5,command=lambda: abrir_ventana_agregar_producto())
boton_agregar_producto.image = agregar
boton_agregar_producto.bind('<Enter>', lambda e: boton_agregar_producto.config(background='RoyalBlue4', foreground='white'))
boton_agregar_producto.bind('<Leave>', lambda e: boton_agregar_producto.config(background='RoyalBlue3', foreground='white'))

boton_agregar_producto.place(x=20,y=100)

#contenedor de busqueda
marco_superior = Frame(ventana, bg="#e5e4fb")
marco_superior.place(x=335,y=110)

# buscar por producto----------
label_nombre = Label(marco_superior, text="Buscar Producto:", bg="#e5e4fb", font=("Arial", 12))
label_nombre.grid(row=0, column=1)
entry_nombre = Entry(marco_superior, font=("Arial", 12), borderwidth=1, relief=SOLID,width=15)
entry_nombre.bind("<KeyRelease>", mayuscula_primera_letra(entry_nombre))
entry_nombre.grid(row=0, column=2, padx=10)

# buscar por categoria-----------------------
label_categoria = Label(marco_superior, text="Categoría:", bg="#e5e4fb", font=("Arial", 12))
label_categoria.grid(row=0, column=3)
combobox_categoria = ttk.Combobox(marco_superior, values=[" ", "categoria 1", "categoria 2"], font=("Arial", 12),width=15)
combobox_categoria.grid(row=0, column=4, padx=10)

# boton de buscar
boton_buscar = Button(marco_superior, text="Buscar", image=buscar, compound=RIGHT,bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"),cursor="hand2")
boton_buscar.image = buscar
boton_buscar.bind('<Enter>', lambda e: boton_buscar.config(background='RoyalBlue4', foreground='white'))
boton_buscar.bind('<Leave>', lambda e: boton_buscar.config(background='RoyalBlue3', foreground='white'))
boton_buscar.grid(row=0, column=5, padx=10)

# Crear un estilo personalizado para la tabla
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 11, "bold"))

# contenedor_tabla---------------------------
marco_tabla = Frame(ventana, bg="#e5e4fb")
marco_tabla.place(x=60,y=200)
#contenedor
frame_contenedor = Frame(marco_tabla, bg="#e5e4fb")
frame_contenedor.pack( padx=2)
#tabla
tabla = ttk.Treeview(frame_contenedor, columns=("id", "nombre", "precio","cantidad", "categoria", "fecha_ingreso"), show="headings", style="Treeview")
tabla.pack(side=LEFT)
#scrollbar
vertical = ttk.Scrollbar(frame_contenedor, orient="vertical", command=tabla.yview)
vertical.pack(side="right", fill=Y)

tabla.configure(yscrollcommand=vertical.set)
# Configurar los encabezados de la tabla
tabla.heading("id", text="ID", anchor=CENTER)
tabla.heading("nombre", text="Nombre", anchor=CENTER)
tabla.heading("precio", text="Precio", anchor=CENTER)
tabla.heading("cantidad", text="Cantidad", anchor=CENTER)
tabla.heading("categoria", text="Categoria", anchor=CENTER)
tabla.heading("fecha_ingreso", text="Fecha de ingreso", anchor=CENTER)
# Ajustar el ancho de las columnas
tabla.column("#0", width=55, stretch=False, anchor=CENTER)
tabla.column("#1", width=55, stretch=True, anchor=CENTER)
tabla.column("#2", width=180, stretch=True, anchor=CENTER)
tabla.column("#3", width=130, stretch=True, anchor=CENTER)
tabla.column("#4", width=130, stretch=True, anchor=CENTER)
tabla.column("#5", width=170, stretch=True, anchor=CENTER)
tabla.column("#6", width=160, stretch=True, anchor=CENTER)


# Contenedor de botones
marco_botones = Frame(ventana, bg="#e5e4fb",height=65)
marco_botones.pack(side=BOTTOM, fill="both",pady=(0,40))

# boton de editar
boton_editar = Button(marco_botones, text="Editar", image=editar, compound=RIGHT,bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"), padx=5, pady=5, width=130,cursor="hand2")
boton_editar.image = editar
boton_editar.bind('<Enter>', lambda e: boton_editar.config(background='RoyalBlue4', foreground='white'))
boton_editar.bind('<Leave>', lambda e: boton_editar.config(background='RoyalBlue3', foreground='white'))
boton_editar.grid(row=0,column=0,padx=10)

# boton de eliminar
boton_eliminar = Button(marco_botones, text="Eliminar", image=eliminar, compound=RIGHT,bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5, width=130,cursor="hand2")
boton_eliminar.image = eliminar
boton_eliminar.bind('<Enter>', lambda e: boton_eliminar.config(background='RoyalBlue4', foreground='white'))
boton_eliminar.bind('<Leave>', lambda e: boton_eliminar.config(background='RoyalBlue3', foreground='white'))
boton_eliminar.grid(row=0,column=1,padx=10)

#boton de reporte
boton_reporte=Button(marco_botones,text="Generar Reporte",image=reporte,compound=RIGHT,bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5,cursor="hand2",width=150 )
boton_reporte.image = reporte
boton_reporte.bind('<Enter>', lambda e: boton_reporte.config(background='RoyalBlue4', foreground='white'))
boton_reporte.bind('<Leave>', lambda e: boton_reporte.config(background='RoyalBlue3', foreground='white'))
boton_reporte.grid(row=0,column=2,padx=10)

def abrir_ventana_actualizar_cantidad():
    ventana_actualizar = Toplevel(ventana)
    ventana_actualizar.title("Actualizar Cantidad del Producto")
    ventana_actualizar.resizable(width=0, height=0)
    ventana_actualizar.config(bg="#e5e4fb")
    centrar_ventana(ventana_actualizar,350, 270)

    ventana_actualizar.iconphoto(True, icono_actualizar)

    # Contenedor para los botones de entrada y salida
    contenedor_botones = Frame(ventana_actualizar, bg="#e5e4fb")
    contenedor_botones.place(x=75,y=80)

    # Función para el botón de entrada
    def actualizar_entrada():
        contenedor_botones.pack_forget()  # Ocultar contenedor de botones
        contenedor_entrada.pack(pady=10)  # Mostrar contenedor de entrada

    # Función para el botón de salida
    def actualizar_salida():
        contenedor_botones.pack_forget()  # Ocultar contenedor de botones
        contenedor_salida.pack(pady=10)  # Mostrar contenedor de salida

    # Botón para la entrada
    boton_entrada = Button(contenedor_botones, image=entrada, compound=RIGHT, text="Registrar Entrada   ", bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"), cursor="hand2", width=190, command=actualizar_entrada)
    boton_entrada.image = entrada
    boton_entrada.pack(pady=10)

    # Botón para la salida
    boton_salida = Button(contenedor_botones, image=salida, compound=RIGHT, text="Registrar Salida   ", bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"), cursor="hand2", width=190, command=actualizar_salida)
    boton_salida.image = salida
    boton_salida.pack(pady=10)

    # Contenedor para la entrada
    contenedor_entrada = LabelFrame(ventana_actualizar, text="Registrar Entrada", fg="RoyalBlue3", font=("Arial", 12, "bold"), bg="#e5e4fb")
    # Agrega tus widgets de entrada aquí...
    # codigo de producto-------------------------------
    codigo = Label(contenedor_entrada, text="ID del producto:",font=("arial",12), bg="#e5e4fb")
    codigo.grid(row=0, column=0, padx=5, pady=10 )      
    # nombre del producto-----------------------------------
    producto = Label(contenedor_entrada, text="Nombre del Producto:",font=("arial",12), bg="#e5e4fb")
    producto.grid(row=1, column=0, padx=5, pady=10)
    entrada_producto = Entry(contenedor_entrada, width=15, font=("arial", 12))
    entrada_producto.focus()
    entrada_producto.grid(row=1, column=1, padx=5, pady=5)
    
    # cantidad existente--------------------------------------------------
    cantidad = Label(contenedor_entrada, text="Cantidad Existente:",font=("arial",12), bg="#e5e4fb")
    cantidad.grid(row=2, column=0, padx=(0, 5), pady=10)
    entrada_cantidad = Entry(contenedor_entrada, width=7, font=("arial", 12))
    entrada_cantidad.grid(row=2, column=1, sticky="W", padx=(0, 5), pady=2)
    
    #cantidad de entrada
    cantidad = Label(contenedor_entrada, text="Cantidad de Entrada:",font=("arial",12), bg="#e5e4fb")
    cantidad.grid(row=3, column=0, padx=(0, 5), pady=10)
    entrada_cantidad = Entry(contenedor_entrada, width=7, font=("arial", 12))
    entrada_cantidad.focus()
    entrada_cantidad.grid(row=3, column=1, sticky="W", padx=(0, 5), pady=2)
    
    # boton guardar producto---------------------------------------------------
    boton = Button(contenedor_entrada, text="Actualizar", font=("arial", 12, "bold"), fg="white", bg="RoyalBlue3",width=10,cursor="hand2")
    boton.grid(row=4, column=0, sticky="ew",padx=5,pady=5)      
    # Botón de "Cancelar"
    cancelar_button = Button(contenedor_entrada, text="Cancelar", font=("arial", 12, "bold"), fg="white", bg="gray30",cursor="hand2",width=10)
    cancelar_button.grid(row=4, column=1, sticky="ew", padx=5,pady=5) 

    # Contenedor para la salida
    contenedor_salida = LabelFrame(ventana_actualizar, text="Registrar Salida", fg="RoyalBlue3", font=("Arial", 12, "bold"), bg="#e5e4fb")
    # Agrega tus widgets de salida aquí...
    # codigo de producto-------------------------------
    codigo = Label(contenedor_salida, text="ID del producto:",font=("arial",12), bg="#e5e4fb")
    codigo.grid(row=0, column=0, padx=5, pady=10)
    # nombre del producto-----------------------------------
    producto = Label(contenedor_salida, text="Nombre del Producto:",font=("arial",12), bg="#e5e4fb")
    producto.grid(row=1, column=0, padx=5, pady=10)
    salida_producto = Entry(contenedor_salida, width=15, font=("arial", 12))
    salida_producto.focus()
    salida_producto.grid(row=1, column=1, padx=5, pady=5)
    
    # cantidad existente--------------------------------------------------
    cantidad = Label(contenedor_salida, text="Cantidad Existente:",font=("arial",12), bg="#e5e4fb")
    cantidad.grid(row=2, column=0, padx=(0, 5), pady=10)
    entrada_cantidad = Entry(contenedor_salida, width=7, font=("arial", 12))
    entrada_cantidad.grid(row=2, column=1, sticky="W", padx=(0, 5), pady=2)
    
    #cantidad de entrada
    cantidad = Label(contenedor_salida, text="Cantidad de Salida:",font=("arial",12), bg="#e5e4fb")
    cantidad.grid(row=3, column=0, padx=(0, 5), pady=10)
    entrada_cantidad = Entry(contenedor_salida, width=7, font=("arial", 12))
    entrada_cantidad.focus()
    entrada_cantidad.grid(row=3, column=1, sticky="W", padx=(0, 5), pady=2)
    
    # boton guardar producto---------------------------------------------------
    boton = Button(contenedor_salida, text="Actualizar", font=("arial", 12, "bold"), fg="white", bg="RoyalBlue3",width=10,cursor="hand2")
    boton.grid(row=4, column=0, sticky="ew",padx=5,pady=5)
    # Botón de "Cancelar"
    cancelar_button = Button(contenedor_salida, text="Cancelar", font=("arial", 12, "bold"), fg="white", bg="gray30",cursor="hand2",width=10)
    cancelar_button.grid(row=4, column=1, sticky="ew", padx=5,pady=5)

#boton de actualizar
boton_actualizar=Button(marco_botones,text="Actualizar Cantidad",image=actualizar,compound=RIGHT,bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5,cursor="hand2",width=168,command=lambda: abrir_ventana_actualizar_cantidad() )
boton_actualizar.image = actualizar
boton_actualizar.bind('<Enter>', lambda e: boton_actualizar.config(background='RoyalBlue4', foreground='white'))
boton_actualizar.bind('<Leave>', lambda e: boton_actualizar.config(background='RoyalBlue3', foreground='white'))
boton_actualizar.grid(row=0,column=3,padx=10)


# boton de salir------------
salir=Button(marco_botones,text="Salir",image=salir,compound=RIGHT,bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5,cursor="hand2",width=100,command=lambda: salir_aplicacion(ventana))
salir.image = salir
salir.bind('<Enter>', lambda e: salir.config(background='RoyalBlue4', foreground='white'))
salir.bind('<Leave>', lambda e: salir.config(background='RoyalBlue3', foreground='white'))
salir.grid(row=0,column=4,padx=(110,0))






ventana.mainloop()
