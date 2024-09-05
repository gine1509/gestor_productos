from tkinter import *
from datetime import datetime
from tkinter import messagebox
from tkinter import ttk
from funciones import *
from conexion import *
from login import inicio_sesion

if not inicio_sesion():  
    exit()
  
      

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
        entrada_codigo = Entry(con_formulario, width=4, font=("arial", 12))
        entrada_codigo.grid(row=0, column=1, sticky="W", padx=(0, 5), pady=2)

        # Asignar ID automáticamente
        ultimo_id = obtener_ultimo_id()
        entrada_codigo.insert(0, ultimo_id)
        entrada_codigo.config(state="readonly")

        # nombre del producto-----------------------------------
        producto = Label(con_formulario, text="Nombre del Producto:",font=("arial",12), bg="#e5e4fb")
        producto.grid(row=1, column=0, padx=5, pady=10)
        entrada_producto = Entry(con_formulario, width=20, font=("arial", 12))
        entrada_producto.bind("<KeyRelease>", mayuscula_primera_letra(entrada_producto))
        entrada_producto.focus()
        entrada_producto.grid(row=1, column=1, padx=5, pady=5)

        # precio -------------------------------------------------------------
        precio_venta = Label(con_formulario, text="Precio del Producto:", font=("arial",12), bg="#e5e4fb")
        precio_venta.grid(row=2, column=0, padx=5, pady=10)
        entrada_precio = Entry(con_formulario, width=7, font=("arial", 12))
        solo_numeros(entrada_precio)
        entrada_precio.grid(row=2, column=1, sticky="W", padx=(0, 5), pady=2)

        # cantidad --------------------------------------------------
        cantidad = Label(con_formulario, text="Cantidad Inicial:",font=("arial",12), bg="#e5e4fb")
        cantidad.grid(row=3, column=0, padx=(0, 5), pady=10)
        entrada_cantidad = Entry(con_formulario, width=7, font=("arial", 12))
        solo_numeros(entrada_cantidad)
        entrada_cantidad.grid(row=3, column=1, sticky="W", padx=(0, 5), pady=2)

        # categoria-------------------------------------------------------------
        categoria = Label(con_formulario, text="Categoría del Producto:",font=("arial",12), bg="#e5e4fb")
        categoria.grid(row=4, column=0, padx=0, pady=10)
        categorias = obtener_categorias_buscar()
        menu = ttk.Combobox(con_formulario, values=[f"{id_categoria} - {nombre_categoria}" for id_categoria, nombre_categoria in categorias],  font=("arial", 12))
        menu.set("Seleccione")
        menu.config(state="readonly")
        menu.config(width=12)
        menu.grid(row=4, column=1, sticky="W", padx=(0, 5), pady=5)
        
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
            
            categorias = mostrar_categorias()
            def guardar_categoria():
                nombre_categoria = entrada_categoria.get()
                if not verificar_nombre_categoria(nombre_categoria,ventana_categoria):
                    return
                if not nombre_categoria:
                    messagebox.showerror("Error", "Debe llenar el campo de nombre de categoría")
                    return
                agregar_categoria(nombre_categoria)
                entrada_categoria.delete(0, END)
                
                # Actualizar la variable global con los nuevos datos
                global categorias
                categorias = mostrar_categorias()
                
                # Refrescar la tabla
                categorias_treeview.delete(*categorias_treeview.get_children())
                for categoria in mostrar_categorias():
                    categorias_treeview.insert("", "end", values=categoria)
                messagebox.showinfo("Éxito", "Categoría agregada correctamente",parent=ventana_categoria)    

            boton_guardar_categoria = Button(con_formulario_categoria, text="Guardar Categoría", font=("arial", 10, "bold"), fg="white", bg="RoyalBlue3", cursor="hand2", width=10,command=guardar_categoria)
            boton_guardar_categoria.grid(row=1, column=0,sticky="ew", padx=10, pady=5)

            boton_cancelar_categoria = Button(con_formulario_categoria, text="Cancelar", font=("arial", 10, "bold"), fg="white", bg="gray30", cursor="hand2", width=10, command=lambda: cancelar_categoria(entrada_categoria))
            boton_cancelar_categoria.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

            # Buscar categorías
            buscar_categoria_label = Label(ventana_categoria, text="Buscar Categoría:", font=("arial", 10), bg="#e5e4fb")
            buscar_categoria_label.place(x=125,y=143)

            buscar_categoria_entry = Entry(ventana_categoria, width=20, font=("arial", 10))
            buscar_categoria_entry.bind("<KeyRelease>", mayuscula_primera_letra(buscar_categoria_entry))
            buscar_categoria_entry.place(x=245,y=145)

            buscar_categoria_boton = Button(ventana_categoria, image=buscar_cat,compound=RIGHT,text="Buscar", font=("arial", 10, "bold"), fg="white", bg="RoyalBlue3", cursor="hand2", width=65,command=lambda: buscar_categoria(categorias_treeview,buscar_categoria_entry,ventana_categoria))
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
            
            resultados = mostrar_categorias()
            for resultado in resultados:
                categorias_treeview.insert("", "end", values=resultado)

            # Scrollbar
            vertical = ttk.Scrollbar(frame_contenedor, orient="vertical", command=categorias_treeview.yview)
            vertical.pack(side="right", fill=Y)
            categorias_treeview.config(yscrollcommand=vertical.set)
            
            def abrir_ventana_editar_categoria():
                ventana_editar_categoria = Toplevel(ventana_categoria)
                ventana_editar_categoria.title("Editar Categoria")
                ventana_editar_categoria.resizable(width=0, height=0)
                ventana_editar_categoria.config(bg="#e5e4fb")
                centrar_ventana(ventana_editar_categoria,330, 200)
                
                seleccion = categorias_treeview.selection()
                if not seleccion:
                    messagebox.showerror("Error", "No ha seleccionado ninguna categoria", parent=ventana_categoria)
                    return
                
                con_formulario_categoria = LabelFrame(ventana_editar_categoria, text="Editar Categoría", fg="RoyalBlue3", font=("arial", 14, "bold"), bg="#e5e4fb")
                con_formulario_categoria.pack(side=LEFT, fill=BOTH, expand=True,padx=20, pady=20)
                
                # codigo de producto-------------------------------
                codigo = Label(con_formulario_categoria, text="ID de la categoria:",font=("arial",10), bg="#e5e4fb")
                codigo.grid(row=0, column=0, padx=5, pady=10)
                entrada_codigo = Entry(con_formulario_categoria, width=4, font=("arial", 12))
                entrada_codigo.grid(row=0, column=1, sticky="W", padx=(0, 5), pady=2)

                categoria_label = Label(con_formulario_categoria, text="Nombre de la Categoría:", font=("arial", 10), bg="#e5e4fb")
                categoria_label.grid(row=1, column=0, padx=5, pady=10)

                entrada_categoria = Entry(con_formulario_categoria, width=15, font=("arial", 10))
                entrada_categoria.bind("<KeyRelease>", mayuscula_primera_letra(entrada_categoria))
                entrada_categoria.grid(row=1, column=1, padx=5, pady=5)
                
                # Obtener el id del producto seleccionado en la tabla
                id_categoria = categorias_treeview.item(categorias_treeview.selection()[0], 'values')[0]
                
                #Llenar el formulario con los datos de la categoría seleccionada
                llenar_formulario_editar_categoria(id_categoria, entrada_codigo, entrada_categoria)
                
                boton_guardar_categoria = Button(con_formulario_categoria, text="Guardar Categoría", font=("arial", 10, "bold"), fg="white", bg="RoyalBlue3", cursor="hand2", width=10,command=lambda: actualizar_categoria(entrada_categoria,ventana_editar_categoria,categorias_treeview))
                boton_guardar_categoria.grid(row=2, column=0,sticky="ew", padx=10, pady=5)

                boton_cancelar_categoria = Button(con_formulario_categoria, text="Cancelar", font=("arial", 10, "bold"), fg="white", bg="gray30", cursor="hand2", width=10, command=lambda: cancelar_categoria(ventana_editar_categoria))
                boton_cancelar_categoria.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

            # Botones de editar y eliminar
            editar_categoria_boton = Button(ventana_categoria,image=editar_cat, compound=RIGHT, text="Editar", font=("arial", 10, "bold"), fg="white", bg="RoyalBlue3", cursor="hand2", width=75,command=lambda: abrir_ventana_editar_categoria())
            editar_categoria_boton.image=editar_cat
            editar_categoria_boton.place(x=255,y=280)

            eliminar_categoria_boton = Button(ventana_categoria,image=eliminar_cat,compound=RIGHT, text="Eliminar", font=("arial", 10, "bold"), fg="white", bg="RoyalBlue3", cursor="hand2", width=75,command=lambda: eliminar_categoria(categorias_treeview,ventana_categoria))
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
        
        productos = mostrar_productos()
        def guardar_producto():
            id_producto = entrada_codigo.get()
            nombre_producto = entrada_producto.get()
            if not verificar_nombre_producto(nombre_producto, ventana_agregar):
                return 
            precio_producto = entrada_precio.get()
            cantidad_producto = entrada_cantidad.get()
            categoria_producto = menu.get()

            if not validar_campos(nombre_producto, precio_producto, cantidad_producto, categoria_producto, ventana_agregar):
                return  # Si hay un error, no se hace nada más
            # Verificar si la categoría ha sido seleccionada
            if categoria_producto =="Seleccione":
                messagebox.showerror("Error", "Debe seleccionar una categoría", parent=ventana_agregar)
                return

            try:
                agregar_producto(nombre_producto, precio_producto, cantidad_producto, categoria_producto)
                ventana_agregar.destroy()
                # Actualizar la variable global con los nuevos datos
                global productos
                productos = mostrar_productos()
                # Refrescar la tabla
                tabla.delete(*tabla.get_children())
                for producto in mostrar_productos():
                    tabla.insert("", "end", values=producto)
            except pymysql.Error as e:
                messagebox.showerror("Error", "Error al agregar producto: {}".format(e))

            

        # boton guardar producto---------------------------------------------------
        boton = Button(con_formulario, text="Guardar Producto", font=("arial", 12, "bold"), fg="white", bg="RoyalBlue3",width=20,cursor="hand2",command=guardar_producto)
        boton.grid(row=5, column=0, sticky="ew",padx=10,pady=5)

        # Botón de "Cancelar"
        cancelar_button = Button(con_formulario, text="Cancelar", font=("arial", 12, "bold"), fg="white", bg="gray30",cursor="hand2",command=lambda: salir_aplicacion(ventana_agregar))
        cancelar_button.grid(row=5, column=1, sticky="ew", padx=10,pady=5)  



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
categorias = obtener_categorias_buscar()
combobox_categoria = ttk.Combobox(marco_superior, values=[""] + [f"{id_categoria} - {nombre_categoria}" for id_categoria, nombre_categoria in categorias], font=("Arial", 12),width=15)
combobox_categoria.grid(row=0, column=4, padx=10)

# boton de buscar
boton_buscar = Button(marco_superior, text="Buscar", image=buscar, compound=RIGHT,bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"),cursor="hand2",command=lambda: buscar_productos(tabla, entry_nombre, combobox_categoria))
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

resultados = mostrar_productos()
for resultado in resultados:
    tabla.insert("", "end", values=resultado)


# Contenedor de botones
marco_botones = Frame(ventana, bg="#e5e4fb",height=65)
marco_botones.pack(side=BOTTOM, fill="both",pady=(0,40))

# funcion para abrir el formulario de editar producto
def abrir_ventana_editar_producto():
        ventana_editar = Toplevel(ventana)
        ventana_editar.title("Editar Producto")
        ventana_editar.resizable(width=0, height=0)
        ventana_editar.config(bg="#e5e4fb")
        centrar_ventana(ventana_editar,480, 370)
        
        seleccion = tabla.selection()
        if not seleccion:
            messagebox.showerror("Error", "No ha seleccionado ningún producto")
            return

        

        # contenedor del formulario----------------------------------------
        con_formulario = LabelFrame(ventana_editar, text="Editar Producto",fg="RoyalBlue3", font=("arial", 20, "bold"), bg="#e5e4fb")
        con_formulario.pack(side=LEFT, fill=BOTH, expand=True,padx=20, pady=20)
        
        # codigo de producto-------------------------------
        codigo = Label(con_formulario, text="ID del producto:",font=("arial",12), bg="#e5e4fb")
        codigo.grid(row=0, column=0, padx=5, pady=10)
        entrada_codigo = Entry(con_formulario, width=4, font=("arial", 12))
        entrada_codigo.grid(row=0, column=1, sticky="W", padx=(0, 5), pady=2)

        # nombre del producto-----------------------------------
        producto = Label(con_formulario, text="Nombre del Producto:",font=("arial",12), bg="#e5e4fb")
        producto.grid(row=1, column=0, padx=5, pady=10)
        entrada_producto = Entry(con_formulario, width=20, font=("arial", 12))
        entrada_producto.bind("<KeyRelease>", mayuscula_primera_letra(entrada_producto))
        entrada_producto.grid(row=1, column=1, padx=5, pady=5)

        # precio -------------------------------------------------------------
        precio_venta = Label(con_formulario, text="Precio del Producto:", font=("arial",12), bg="#e5e4fb")
        precio_venta.grid(row=2, column=0, padx=5, pady=10)
        entrada_precio = Entry(con_formulario, width=7, font=("arial", 12))
        solo_numeros(entrada_precio)
        entrada_precio.grid(row=2, column=1, sticky="W", padx=(0, 5), pady=2)

        # cantidad --------------------------------------------------
        cantidad = Label(con_formulario, text="Cantidad Inicial:",font=("arial",12), bg="#e5e4fb")
        cantidad.grid(row=3, column=0, padx=(0, 5), pady=10)
        entrada_cantidad = Entry(con_formulario, width=7, font=("arial", 12))
        solo_numeros(entrada_cantidad)
        entrada_cantidad.grid(row=3, column=1, sticky="W", padx=(0, 5), pady=2)

        # categoria-------------------------------------------------------------
        categoria = Label(con_formulario, text="Categoría del Producto:",font=("arial",12), bg="#e5e4fb")
        categoria.grid(row=4, column=0, padx=0, pady=10)
        categorias = obtener_categorias_buscar()
        menu = ttk.Combobox(con_formulario, values=[f"{id_categoria} - {nombre_categoria}" for id_categoria, nombre_categoria in categorias],  font=("arial", 12))
        menu.config(width=12)
        menu.grid(row=4, column=1, sticky="W", padx=(0, 5), pady=5)
        
        
        # Obtener el id del producto seleccionado en la tabl
        id_producto = tabla.item(tabla.selection()[0], 'values')[0]
        # Llamar a la función para llenar el formulario
        llenar_formulario_editar_producto(id_producto, con_formulario)
        
        # boton actualizar producto---------------------------------------------------
        boton = Button(con_formulario, text="Actualizar Producto", font=("arial", 12, "bold"), fg="white", bg="RoyalBlue3",width=20,cursor="hand2",command=lambda: actualizar_producto(entrada_codigo,entrada_producto,entrada_precio,entrada_cantidad,menu,ventana_editar,tabla))
        
        boton.grid(row=5, column=0, sticky="ew",padx=10,pady=5)

        # Botón de "Cancelar"
        cancelar_button = Button(con_formulario, text="Cancelar", font=("arial", 12, "bold"), fg="white", bg="gray30",cursor="hand2",command=lambda: salir_aplicacion(ventana_editar))
        cancelar_button.grid(row=5, column=1, sticky="ew", padx=10,pady=5)

# boton de editar
boton_editar = Button(marco_botones, text="Editar", image=editar, compound=RIGHT,bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"),pady=5, width=120,cursor="hand2",command=lambda: abrir_ventana_editar_producto())
boton_editar.image = editar
boton_editar.bind('<Enter>', lambda e: boton_editar.config(background='RoyalBlue4', foreground='white'))
boton_editar.bind('<Leave>', lambda e: boton_editar.config(background='RoyalBlue3', foreground='white'))
boton_editar.grid(row=0,column=0,padx=5)



# boton de eliminar
boton_eliminar = Button(marco_botones, text="Eliminar", image=eliminar, compound=RIGHT,bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"),pady=5, width=120,cursor="hand2",command=lambda: eliminar_producto(tabla))
boton_eliminar.image = eliminar
boton_eliminar.bind('<Enter>', lambda e: boton_eliminar.config(background='RoyalBlue4', foreground='white'))
boton_eliminar.bind('<Leave>', lambda e: boton_eliminar.config(background='RoyalBlue3', foreground='white'))
boton_eliminar.grid(row=0,column=1,padx=5)


def abrir_ventana_registrar_entrada():
    ventana_entrada = Toplevel(ventana)
    ventana_entrada.title("Registrar Entrada del Producto")
    ventana_entrada.resizable(width=0, height=0)
    ventana_entrada.config(bg="#e5e4fb")
    centrar_ventana(ventana_entrada,350, 270)
    ventana_entrada.iconphoto(True, icono_actualizar)
    
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showerror("Error", "No ha seleccionado ningun producto",parent=ventana)
        return
    else:
        id_producto = tabla.item(seleccion[0], "values")[0]
    
    contenedor_entrada = LabelFrame(ventana_entrada, text="Registrar Entrada", fg="RoyalBlue3", font=("Arial", 12, "bold"), bg="#e5e4fb")
    contenedor_entrada.pack(side=LEFT, fill=BOTH, expand=True,padx=10, pady=10)
    
    # codigo de producto-------------------------------
    codigo = Label(contenedor_entrada, text="ID del producto:",font=("arial",12), bg="#e5e4fb")
    codigo.grid(row=0, column=0, padx=5, pady=10 ) 
    entrada_codigo = Entry(contenedor_entrada, width=4, font=("arial", 12))
    entrada_codigo.grid(row=0, column=1, sticky="W", padx=(0, 5), pady=2)     
    # nombre del producto-----------------------------------
    producto = Label(contenedor_entrada, text="Nombre del Producto:",font=("arial",12), bg="#e5e4fb")
    producto.grid(row=1, column=0, padx=5, pady=10)
    entrada_producto = Entry(contenedor_entrada, width=15, font=("arial", 12))
    entrada_producto.grid(row=1, column=1, padx=5, pady=5)
    
    # cantidad existente--------------------------------------------------
    cantidad = Label(contenedor_entrada, text="Cantidad Existente:",font=("arial",12), bg="#e5e4fb")
    cantidad.grid(row=2, column=0, padx=(0, 5), pady=10)
    entrada_cantidad = Entry(contenedor_entrada, width=7, font=("arial", 12))
    entrada_cantidad.grid(row=2, column=1, sticky="W", padx=(0, 5), pady=2)
    
    llenar_formulario_registrar_entrada(id_producto,entrada_codigo,entrada_producto,entrada_cantidad, contenedor_entrada,ventana_entrada) 
    
    #cantidad de entrada
    cantidad = Label(contenedor_entrada, text="Cantidad de Entrada:",font=("arial",12), bg="#e5e4fb")
    cantidad.grid(row=3, column=0, padx=(0, 5), pady=10)
    entrada_cantidad_e = Entry(contenedor_entrada, width=7, font=("arial", 12))
    entrada_cantidad_e.focus()
    solo_numeros(entrada_cantidad_e)
    entrada_cantidad_e.grid(row=3, column=1, sticky="W", padx=(0, 5), pady=2)
    
    
    # boton guardar producto---------------------------------------------------
    boton = Button(contenedor_entrada, text="Actualizar", font=("arial", 12, "bold"), fg="white", bg="RoyalBlue3",width=10,cursor="hand2",command=lambda: registrar_entrada_producto(id_producto,int(entrada_cantidad_e.get()),ventana_entrada,tabla))
    boton.grid(row=4, column=0, sticky="ew",padx=5,pady=5)
    
    # Botón de "Cancelar"
    cancelar_button = Button(contenedor_entrada, text="Cancelar", font=("arial", 12, "bold"), fg="white", bg="gray30",cursor="hand2",width=10,command=lambda: salir_aplicacion(ventana_entrada))
    cancelar_button.grid(row=4, column=1, sticky="ew", padx=5,pady=5) 

#boton de registrar entrada
boton_entrada = Button(marco_botones, image=entrada, compound=RIGHT, text="Registrar Entrada ", bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"),pady=5, cursor="hand2", width=170,command=lambda: abrir_ventana_registrar_entrada())
boton_entrada.image = entrada
boton_entrada.bind('<Enter>', lambda e: boton_entrada.config(background='RoyalBlue4', foreground='white'))
boton_entrada.bind('<Leave>', lambda e: boton_entrada.config(background='RoyalBlue3', foreground='white'))
boton_entrada.grid(row=0,column=2,padx=5)

def abrir_ventana_registrar_salida():
    ventana_salida = Toplevel(ventana)
    ventana_salida.title("Registrar Salida del Producto")
    ventana_salida.resizable(width=0, height=0)
    ventana_salida.config(bg="#e5e4fb")
    centrar_ventana(ventana_salida,350, 270)
    ventana_salida.iconphoto(True, icono_actualizar)
    
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showerror("Error", "No ha seleccionado ningun producto",parent=ventana)
        return
    else:
        id_producto = tabla.item(seleccion[0], "values")[0]
        
        
        
        
        
    contenedor_salida = LabelFrame(ventana_salida, text="Registrar Salida", fg="RoyalBlue3", font=("Arial", 12, "bold"), bg="#e5e4fb")
    contenedor_salida.pack(side=LEFT, fill=BOTH, expand=True,padx=10, pady=10)
    
       
    
    # codigo de producto-------------------------------
    codigo = Label(contenedor_salida, text="ID del producto:",font=("arial",12), bg="#e5e4fb")
    codigo.grid(row=0, column=0, padx=5, pady=10 ) 
    entrada_codigo = Entry(contenedor_salida, width=4, font=("arial", 12))
    entrada_codigo.grid(row=0, column=1, sticky="W", padx=(0, 5), pady=2) 
    
       
    # nombre del producto-----------------------------------
    producto = Label(contenedor_salida, text="Nombre del Producto:",font=("arial",12), bg="#e5e4fb")
    producto.grid(row=1, column=0, padx=5, pady=10)
    entrada_producto = Entry(contenedor_salida, width=15, font=("arial", 12))
    entrada_producto.grid(row=1, column=1, padx=5, pady=5)
    
    # cantidad existente--------------------------------------------------
    cantidad = Label(contenedor_salida, text="Cantidad Existente:",font=("arial",12), bg="#e5e4fb")
    cantidad.grid(row=2, column=0, padx=(0, 5), pady=10)
    entrada_cantidad = Entry(contenedor_salida, width=7, font=("arial", 12))
    entrada_cantidad.grid(row=2, column=1, sticky="W", padx=(0, 5), pady=2)
    
    llenar_formulario_registrar_salida(id_producto,entrada_codigo,entrada_producto,entrada_cantidad, contenedor_salida,ventana_salida) 
    
    #cantidad de entrada
    cantidad = Label(contenedor_salida, text="Cantidad de Salida:",font=("arial",12), bg="#e5e4fb")
    cantidad.grid(row=3, column=0, padx=(0, 5), pady=10)
    entrada_cantidad_e = Entry(contenedor_salida, width=7, font=("arial", 12))
    entrada_cantidad_e.focus()
    solo_numeros(entrada_cantidad_e)
    entrada_cantidad_e.grid(row=3, column=1, sticky="W", padx=(0, 5), pady=2)
    boton = Button(contenedor_salida, text="Actualizar", font=("arial", 12, "bold"), fg="white", bg="RoyalBlue3",width=10,cursor="hand2", )
    boton.grid(row=4, column=0, sticky="ew",padx=5,pady=5)
    
    # boton guardar producto---------------------------------------------------
    boton = Button(contenedor_salida, text="Actualizar", font=("arial", 12, "bold"), fg="white", bg="RoyalBlue3",width=10,cursor="hand2",command=lambda: registrar_salida_producto(id_producto,int(entrada_cantidad_e.get()),ventana_salida,tabla))
    boton.grid(row=4, column=0, sticky="ew",padx=5,pady=5)
    
    # Botón de "Cancelar"
    cancelar_button = Button(contenedor_salida, text="Cancelar", font=("arial", 12, "bold"), fg="white", bg="gray30",cursor="hand2",width=10,command=lambda: salir_aplicacion(ventana_salida))
    cancelar_button.grid(row=4, column=1, sticky="ew", padx=5,pady=5)

#boton de registrar salida
boton_salida = Button(marco_botones, image=salida, compound=RIGHT, text="Registrar Salida ", bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"), pady=5,cursor="hand2", width=170,command=lambda:abrir_ventana_registrar_salida())
boton_salida.image = salida
boton_salida.bind('<Enter>', lambda e: boton_salida.config(background='RoyalBlue4', foreground='white'))
boton_salida.bind('<Leave>', lambda e: boton_salida.config(background='RoyalBlue3', foreground='white'))
boton_salida.grid(row=0,column=3,padx=5)



#boton de reporte
boton_reporte=Button(marco_botones,text="Generar Reporte",image=reporte,compound=RIGHT,bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"),pady=5,cursor="hand2",width=150,command=lambda: generar_reporte() )
boton_reporte.image = reporte
boton_reporte.bind('<Enter>', lambda e: boton_reporte.config(background='RoyalBlue4', foreground='white'))
boton_reporte.bind('<Leave>', lambda e: boton_reporte.config(background='RoyalBlue3', foreground='white'))
boton_reporte.grid(row=0,column=4,padx=5)

# boton de salir------------
salir=Button(marco_botones,text="Salir",image=salir,compound=RIGHT,bg="RoyalBlue3", fg="white", font=("Arial", 12, "bold"),pady=5,cursor="hand2",width=100,command=lambda: salir_aplicacion(ventana))
salir.image = salir
salir.bind('<Enter>', lambda e: salir.config(background='RoyalBlue4', foreground='white'))
salir.bind('<Leave>', lambda e: salir.config(background='RoyalBlue3', foreground='white'))
salir.grid(row=0,column=5,padx=(60,0))








ventana.mainloop()
