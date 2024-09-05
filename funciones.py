from datetime import datetime
from tkinter import ttk
from tkinter import *
from conexion import *
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas




#funcion para centrar la ventana
def centrar_ventana(ventana,ancho_ventana,alto_ventana):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2)
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    
# Función para actualizar la hora y la fecha
def actualizar_hora(fecha_label,hora_label):
    ahora = datetime.now()
    fecha_actual = ahora.strftime("%d/%m/%Y")  
    hora_actual = ahora.strftime("%I:%M %p")   
    fecha_label.config(text=fecha_actual)
    hora_label.config(text=hora_actual)
    hora_label.after(1000, actualizar_hora, fecha_label, hora_label)
    

# funcion para salir
def salir_aplicacion(ventana):
    ventana.destroy() 

#funcion para limpiar entry    
def cancelar_categoria(entrada_categoria):
    entrada_categoria.delete(0, END)     

#funcion para convertir la primera letra en mayuscula    
def mayuscula_primera_letra(entry):
    
    def callback(evento):
        texto = entry.get()
        palabras = texto.split()
        palabras_mayusculas = [palabra.capitalize() for palabra in palabras]
        entry.delete(0, END)
        entry.insert(0, ' '.join(palabras_mayusculas))
    return callback

#funcion para que ingrese solo numeros
def solo_numeros(entry):
    def callback(P):
        if P == '':
            return True
        try:
            int(P)
            return True
        except ValueError:
            return False
    vcmd = (entry.register(callback), '%P')
    entry.config(validate='key', validatecommand=vcmd)    
    
#funcion para mostrar los registro de la base de datos en la tabla (productos)
def mostrar_productos():
    db = conectar_db()
    cursor = db.cursor()
    query = "SELECT * FROM productos"
    cursor.execute(query)
    resultados = cursor.fetchall()
    db.close()
    return resultados   

#funcion para mostrar los registro de la base de datos en la tabla (categorias)
def mostrar_categorias():
    db = conectar_db()
    cursor = db.cursor()
    query = "SELECT * FROM categorias"
    cursor.execute(query)
    resultados = cursor.fetchall()
    db.close()
    return resultados 




#funcion para mostrar el id con el nombre de la categoria para el menu de buscar    
def obtener_categorias_buscar():
    db = conectar_db()
    cursor = db.cursor()
    query = "SELECT id_categoria, nombre_categoria FROM categorias"
    cursor.execute(query)
    categorias = [(categoria[0], categoria[1]) for categoria in cursor.fetchall()]
    return categorias

#funcion para el id
def obtener_ultimo_id():
    db = conectar_db()
    cursor = db.cursor()
    cursor.execute("SELECT MAX(id_producto) FROM productos")
    ultimo_id = cursor.fetchone()[0]
    if ultimo_id is None:
        ultimo_id = 1
    else:
        ultimo_id += 1
    return ultimo_id
 


#funcion para validar los camppos del fromulario producto

def validar_campos(nombre_producto, precio_producto, cantidad_producto, categoria_producto, ventana):
    if not nombre_producto or not precio_producto or not cantidad_producto or not categoria_producto:
        messagebox.showerror("Error", "Por favor, llene todos los campos", parent=ventana)
        return False
    return True

# funcion para agregar el producto a la base de datos

def agregar_producto(nombre_producto, precio_producto, cantidad_producto, id_categoria):
    db = conectar_db()
    cursor = db.cursor()
    try:
        query = "INSERT INTO productos (nombre_producto, precio_producto, cantidad_producto, id_categoria, fecha_ingreso) VALUES (%s, %s, %s, %s, NOW())"
        values = (nombre_producto, precio_producto, cantidad_producto, id_categoria)
        cursor.execute(query, values)
        db.commit()  
    except pymysql.Error as e:
        db.rollback()
        raise  
    finally:
        cursor.close()
        db.close()  
    mostrar_mensaje_confirmacion("Producto agregado exitosamente!")
    
    
    
    
#funcion para mandar un mensaje de confirmacion
def mostrar_mensaje_confirmacion(mensaje):
    messagebox.showinfo("Confirmación", mensaje)

#funcion para agregar la categoria a la base de datos    
def agregar_categoria(nombre_categoria):
    conn = conectar_db()
    cursor = conn.cursor()
    query = "INSERT INTO categorias (nombre_categoria) VALUES (%s)"
    cursor.execute(query, (nombre_categoria,))
    conn.commit()
    conn.close() 

#funcion para validar el nombre del producto    
def verificar_nombre_producto(nombre_producto,ventana_agregar):
    conn = conectar_db()
    cursor = conn.cursor()
    query = "SELECT * FROM productos WHERE nombre_producto = %s"
    cursor.execute(query, (nombre_producto,))
    if cursor.fetchone():
        
        messagebox.showerror("Error", "El producto ya existe en la base de datos", parent=ventana_agregar)
        return False
    else:
        
        return True

    cursor.close()
    conn.close() 
    
    
    
#funcion para validar el nombre de la categoria    
def verificar_nombre_categoria(nombre_categoria,ventana_agregar):
    conn = conectar_db()
    cursor = conn.cursor()
    query = "SELECT * FROM categorias WHERE nombre_categoria = %s"
    cursor.execute(query, (nombre_categoria,))
    if cursor.fetchone():
        
        messagebox.showerror("Error", "La categoria ya existe en la base de datos", parent=ventana_agregar)
        return False
    else:
        
        return True

    cursor.close()
    conn.close() 
    

# Función de búsqueda de productos
def buscar_productos(tabla, entry_nombre, combobox_categoria):
    db = conectar_db()
    nombre_producto = entry_nombre.get()
    id_categoria = combobox_categoria.get().split(" - ")[0] if combobox_categoria.get() else None
    try:
        cursor = db.cursor()
        query = "SELECT p.id_producto, p.nombre_producto, p.precio_producto, p.cantidad_producto, c.nombre_categoria, p.fecha_ingreso " \
                "FROM productos p " \
                "INNER JOIN categorias c ON p.id_categoria = c.id_categoria "

        if nombre_producto:
            query += "WHERE p.nombre_producto LIKE %s "
            params = (f"%{nombre_producto}%",)
        elif id_categoria:
            query += "WHERE p.id_categoria = %s "
            params = (id_categoria,)
        elif nombre_producto and id_categoria:
            query += "WHERE p.nombre_producto LIKE %s AND p.id_categoria = %s "
            params = (f"%{nombre_producto}%", id_categoria)

        cursor.execute(query, params)
        resultados = cursor.fetchall()

        if not resultados:
            messagebox.showerror("Error", "El producto no existe o la palabra es incorrecta")
        else:
            cursor.close()
            tabla.delete(*tabla.get_children())
            for resultado in resultados:
                tabla.insert("", "end", values=resultado)

            entry_nombre.delete(0, END)
            combobox_categoria.set("")

    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error al buscar productos: {e}")

#funcion para buscar categorias         
        
def buscar_categoria(tabla, buscar_categoria_entry,ventana):
    db = conectar_db()
    try:
        cursor = db.cursor()
        texto_busqueda = buscar_categoria_entry.get()
        cursor.execute("SELECT * FROM categorias WHERE nombre_categoria LIKE %s", ('%' + texto_busqueda + '%',))
        resultados = cursor.fetchall()

        if resultados:
           
            tabla.delete(*tabla.get_children())

            
            for resultado in resultados:
                tabla.insert("", "end", values=resultado)

            
            buscar_categoria_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "La categoría '{}' no existe".format(texto_busqueda),parent=ventana)

        
        db.close()

    except pymysql.Error as e:
        messagebox.showerror("Error", "Error al buscar categoría: {}".format(e))


#funcion para llenar el formulario para editar
def llenar_formulario_editar_producto(id_producto, formulario):
    
    conn = conectar_db()
    cursor = conn.cursor()

    
    cursor.execute("SELECT p.id_producto, p.nombre_producto, p.precio_producto, p.cantidad_producto, c.id_categoria, c.nombre_categoria FROM productos p JOIN categorias c ON p.id_categoria = c.id_categoria WHERE p.id_producto = %s", (id_producto,))
    producto = cursor.fetchone()

    
    for widget in formulario.winfo_children():
        if isinstance(widget, Entry):
            if widget.grid_info()['row'] == 0 and widget.grid_info()['column'] == 1:
                widget.delete(0, END)
                widget.insert(0, producto[0])
                widget.config(state='readonly')  
            elif widget.grid_info()['row'] == 1 and widget.grid_info()['column'] == 1:
                widget.delete(0, END)
                widget.insert(0, producto[1])
            elif widget.grid_info()['row'] == 2 and widget.grid_info()['column'] == 1:
                widget.delete(0, END)
                widget.insert(0, producto[2])
            elif widget.grid_info()['row'] == 3 and widget.grid_info()['column'] == 1:
                widget.delete(0, END)
                widget.insert(0, producto[3])

    
    combobox = next(widget for widget in formulario.winfo_children() if isinstance(widget, ttk.Combobox))

    
    cursor.execute("SELECT id_categoria, nombre_categoria FROM categorias")
    categorias = cursor.fetchall()

    
    combobox['values'] = [f"{id_categoria} - {nombre_categoria}" for id_categoria, nombre_categoria in categorias]

    
    combobox.set(f"{producto[4]} - {producto[5]}")

   
    conn.close()
    

# Función para actualizar el producto
productos = mostrar_productos()
def actualizar_producto(entrada_codigo, entrada_producto, entrada_precio, entrada_cantidad, menu,ventana_editar,tabla):
    
    id_producto = entrada_codigo.get()
    nombre_producto = entrada_producto.get()
    precio_producto = entrada_precio.get()
    cantidad_producto = entrada_cantidad.get()
    categoria_producto = menu.get()

    
    if not id_producto or not nombre_producto or not precio_producto or not cantidad_producto or not categoria_producto:
        messagebox.showerror("Error", "Todos los campos deben estar llenos")
        return

    
    conn = conectar_db()
    cursor = conn.cursor()

    
    cursor.execute("UPDATE productos SET nombre_producto = %s, precio_producto = %s, cantidad_producto = %s, id_categoria = %s WHERE id_producto = %s",
                   (nombre_producto, precio_producto, cantidad_producto, categoria_producto.split(' - ')[0], id_producto))

    conn.commit()
    conn.close()
    messagebox.showinfo("Éxito", "El producto se actualizó exitosamente")

    
    ventana_editar.destroy()
    global productos
    productos = mostrar_productos()
   
    tabla.delete(*tabla.get_children())
    for producto in mostrar_productos():
        tabla.insert("", "end", values=producto)
    
    

# Función para llenar el formulario de edición de categoría
def llenar_formulario_editar_categoria(id_categoria, entrada_codigo, entrada_categoria):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM categorias WHERE id_categoria = %s", (id_categoria,))
    categoria = cursor.fetchone()

    entrada_codigo.delete(0, END)
    entrada_codigo.insert(0, categoria[0])
    entrada_codigo.config(state='readonly') 
     

    entrada_categoria.delete(0, END)
    entrada_categoria.insert(0, categoria[1])

    global id_categoria_seleccionada
    id_categoria_seleccionada = categoria[0]

    conn.close()

# Función para actualizar la categoría
def actualizar_categoria(entrada_nombre, ventana_editar, categorias_treeview):
    nombre_categoria = entrada_nombre.get()
    if not nombre_categoria:
        messagebox.showerror("Error", "Todos los campos deben estar llenos",parent=ventana_editar)
        return

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("UPDATE categorias SET nombre_categoria = %s WHERE id_categoria = %s", (nombre_categoria, id_categoria_seleccionada))

    conn.commit()
    conn.close()
    messagebox.showinfo("Éxito", "La categoría se actualizó exitosamente",parent=ventana_editar)

    ventana_editar.destroy()
    global categorias
    categorias = mostrar_categorias()
    categorias_treeview.delete(*categorias_treeview.get_children())
    for categoria in mostrar_categorias():
        categorias_treeview.insert("", "end", values=categoria)
        


#funcion para eliminar un producto
def eliminar_producto(tabla):
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showerror("Error", "No ha seleccionado ningún producto")
        return
    else:
        id_producto = tabla.item(seleccion[0], "values")[0]

       
        respuesta = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro de eliminar el producto con ID {id_producto}?")

        if respuesta:
            
            conexion = conectar_db()
            cursor = conexion.cursor()
            query = "DELETE FROM productos WHERE id_producto = %s"
            cursor.execute(query, (id_producto,))
            conexion.commit()
            cursor.close()
            conexion.close()

            tabla.delete(seleccion[0])
        else:
            
            pass        

#funcion para eliminar un categoria
def eliminar_categoria(tabla,ventana):
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showerror("Error", "No ha seleccionado ninguna categoria",parent=ventana)
        return
    else:
        id_categoria = tabla.item(seleccion[0], "values")[0]

       
        respuesta = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro de eliminar la categoria con ID {id_categoria}?",parent=ventana)

        if respuesta:
            
            conexion = conectar_db()
            cursor = conexion.cursor()
            query = "DELETE FROM categorias WHERE id_categoria = %s"
            cursor.execute(query, (id_categoria,))
            conexion.commit()
            cursor.close()
            conexion.close()

            tabla.delete(seleccion[0])
        else:
            
            pass
        
#funcion para llenar el formulario de registrar salida        
def llenar_formulario_registrar_salida(id_producto,entrada_codigo,entrada_producto,entrada_cantidad, contenedor_salida,ventana):
    # Configuración de la conexión a la base de datos
    conexion = conectar_db()
    
    try:
        with conexion.cursor() as cursor:
            # Consulta para obtener los datos del producto
            consulta = "SELECT nombre_producto, cantidad_producto FROM productos WHERE id_producto = %s"
            cursor.execute(consulta, (id_producto,))
            resultado = cursor.fetchone()
            
            if resultado:
                nombre_producto, cantidad_producto = resultado
                
                # Llenar las entradas en el formulario
                entrada_codigo.insert(0, id_producto)  # Llenar ID del producto
                entrada_producto.insert(0, nombre_producto)  # Llenar nombre del producto
                entrada_cantidad.insert(0, cantidad_producto)  # Llenar cantidad existente
                
                entrada_codigo.config(state='readonly')
                entrada_producto.config(state='readonly')
                entrada_cantidad.config(state='readonly')
            else:
                messagebox.showerror("Error", "Producto no encontrado", parent=ventana)
    
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al acceder a la base de datos: {e}", parent=ventana)
    
    finally:
        conexion.close()     
        

#funcion para actualizar la cantidad de salida
productos = mostrar_productos()
def registrar_salida_producto(id_producto, cantidad_salida,ventana,tabla):
    
    
    # Conectar a la base de datos
    conn = conectar_db()
    
    try:
        
        cursor = conn.cursor()
        
        
        cursor.execute("SELECT cantidad_producto FROM productos WHERE id_producto = %s", (id_producto,))
        resultado = cursor.fetchone()
        
        if resultado:
            cantidad_existente = resultado[0]
            if cantidad_salida > cantidad_existente:
                messagebox.showerror("Error", "La cantidad de salida supera la cantidad existente.", parent=ventana)
                return
        
            
            query = "INSERT INTO entradas_salidas (id_producto, tipo_movimiento, cantidad_movimiento, fecha_movimiento) VALUES (%s, 'salida', %s, NOW())"
            cursor.execute(query, (id_producto, cantidad_salida))
            
            # Actualizar la cantidad existente del producto en la tabla productos
            query = "UPDATE productos SET cantidad_producto = cantidad_producto - %s WHERE id_producto = %s"
            cursor.execute(query, (cantidad_salida, id_producto))
        
            # Guardar cambios
            conn.commit()
            messagebox.showinfo("Éxito", "Salida registrada correctamente.", parent=ventana)
        else:
            messagebox.showerror("Error", "Producto no encontrado.", parent=ventana)
    
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al registrar la salida: {e}", parent=ventana)
    finally:
        conn.close()
        ventana.destroy()
        global productos
        productos = mostrar_productos()
    
        tabla.delete(*tabla.get_children())
        for producto in mostrar_productos():
            tabla.insert("", "end", values=producto) 
    
#funcion para llenar el formulario de registrar salida        
def llenar_formulario_registrar_entrada(id_producto,entrada_codigo,entrada_producto,entrada_cantidad, contenedor_salida,ventana):
    # Configuración de la conexión a la base de datos
    conexion = conectar_db()
    
    try:
        with conexion.cursor() as cursor:
            # Consulta para obtener los datos del producto
            consulta = "SELECT nombre_producto, cantidad_producto FROM productos WHERE id_producto = %s"
            cursor.execute(consulta, (id_producto,))
            resultado = cursor.fetchone()
            
            if resultado:
                nombre_producto, cantidad_producto = resultado
                
                # Llenar las entradas en el formulario
                entrada_codigo.insert(0, id_producto)  # Llenar ID del producto
                entrada_producto.insert(0, nombre_producto)  # Llenar nombre del producto
                entrada_cantidad.insert(0, cantidad_producto)  # Llenar cantidad existente
                
                entrada_codigo.config(state='readonly')
                entrada_producto.config(state='readonly')
                entrada_cantidad.config(state='readonly')
            else:
                messagebox.showerror("Error", "Producto no encontrado", parent=ventana)
    
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al acceder a la base de datos: {e}", parent=ventana)
    
    finally:
        conexion.close()
        
#funcion para actualizar la cantidad de entrada
productos = mostrar_productos()
def registrar_entrada_producto(id_producto, cantidad_entrada, ventana, tabla):
    # Conectar a la base de datos
    conn = conectar_db()
    try:
        # Crear cursor
        cursor = conn.cursor()
        
        # Insertar registro de entrada en la tabla entradas_salidas
        query = "INSERT INTO entradas_salidas (id_producto, tipo_movimiento, cantidad_movimiento, fecha_movimiento) VALUES (%s, 'entrada', %s, NOW())"
        cursor.execute(query, (id_producto, cantidad_entrada))
        
        # Actualizar la cantidad existente del producto en la tabla productos
        query = "UPDATE productos SET cantidad_producto = cantidad_producto + %s WHERE id_producto = %s"
        cursor.execute(query, (cantidad_entrada, id_producto))
        
        # Guardar cambios
        conn.commit()
        messagebox.showinfo("Éxito", "Entrada registrada correctamente.", parent=ventana)
    
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al registrar la entrada: {e}", parent=ventana)
    finally:
        conn.close()
        ventana.destroy()
        global productos
        productos = mostrar_productos()
        
        tabla.delete(*tabla.get_children())
        for producto in mostrar_productos():
            tabla.insert("", "end", values=producto) 


def generar_reporte():
    # Conexión a la base de datos
    conexion = conectar_db()
    
    cursor = conexion.cursor()

    # Consulta de productos
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    # Consulta de movimientos
    cursor.execute("SELECT * FROM entradas_salidas")
    movimientos = cursor.fetchall()

    # Crear el PDF
    pdf_filename = "reporte_gestor_productos.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter

    # Títulos
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, "Gestor de Productos")
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, height - 100, "Productos Existentes")
    
    # Tabla de productos
    c.setFont("Helvetica", 12)
    y_position = height - 130
    for producto in productos:
        c.drawString(100, y_position, f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")
        y_position -= 20

    # Título de movimientos
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, y_position - 20, "Movimientos de Salidas y Entradas de Productos")
    
    # Tabla de movimientos
    c.setFont("Helvetica", 12)
    y_position -= 50
    for movimiento in movimientos:
        c.drawString(100, y_position, f"ID: {movimiento[0]}, Producto ID: {movimiento[1]}, Tipo: {movimiento[2]}, Cantidad: {movimiento[3]}, Fecha: {movimiento[4]}")
        y_position -= 20

    # Guardar el PDF
    c.save()
    conexion.close()
                        


        
        
           

    
    
    

  
    