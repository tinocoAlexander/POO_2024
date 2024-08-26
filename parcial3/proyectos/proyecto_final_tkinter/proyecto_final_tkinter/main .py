import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from clases import *

def main():
    def login():
        correo = entrada_correo.get()
        contraseña = entrada_contraseña.get()
        global curp_global

        try:
            # Utilizar la clase Personas para realizar la consulta de login
            query = """
                SELECT CURP_persona, nombre_persona 
                FROM personas 
                WHERE email_persona = %s AND contrasena_persona = %s
            """
            cursor.execute(query, (correo, contraseña))
            persona = cursor.fetchone()
            
            if persona:
                curp = persona[0]
                nombre_usuario = persona[1]
                curp_global = persona[0]

                # Verificar si la persona es estudiante usando la clase Estudiantes
                estudiante = Estudiantes.mostrar()
                estudiante = [e for e in estudiante if e[7] == curp]  # Filtrar por CURP_persona
                if estudiante:
                    matricula = estudiante[0][0]  # Obtener la matrícula del estudiante
                    abrir_menu_estudiante(matricula, nombre_usuario)
                else:
                    # Si no es estudiante, verificamos si es profesor o administrador
                    consulta = "SELECT privilegio FROM profesores WHERE CURP_persona = %s"
                    cursor.execute(consulta, (curp,))
                    privilegio = cursor.fetchone()
                    if privilegio:
                        abrir_menu_profesor(nombre_usuario)
                    else:
                        consulta = "SELECT privilegio FROM administradores WHERE CURP_persona = %s"
                        cursor.execute(consulta, (curp,))
                        privilegio = cursor.fetchone()
                        if privilegio:
                            abrir_menu_administrador(nombre_usuario)
                        else:
                            messagebox.showerror("Error", "Usuario no encontrado en roles.")
            else:
                messagebox.showerror("Error", "Correo o contraseña incorrectos.")

        except Exception as e:
            messagebox.showerror("Error", f"Error al realizar la consulta: {e}")

    def abrir_menu_estudiante(matricula, nombre_usuario):
        ventana.withdraw()  # Oculta la ventana de inicio de sesión
        ventana_estudiante = tk.Toplevel()
        ventana_estudiante.title("Menú Estudiante")
        ventana_estudiante.geometry("900x600")

        # Etiqueta de bienvenida en la parte superior izquierda
        etiqueta_bienvenida = tk.Label(ventana_estudiante, text=f"Bienvenido, {nombre_usuario}", font=("Arial", 14, "bold"))
        etiqueta_bienvenida.pack(anchor="nw", padx=10, pady=10)

        # Frame para los botones de cambiar contraseña y cerrar sesión
        marco_botones = tk.Frame(ventana_estudiante)
        marco_botones.pack(anchor="nw", padx=10, pady=(0, 10))

        # Botón para cambiar contraseña
        boton_cambiar_contraseña = tk.Button(marco_botones, text="Cambiar Contraseña", font=("Arial", 12), bg="#4CAF50", fg="white", command=cambiar_contraseña)
        boton_cambiar_contraseña.pack(side="left", padx=5)

        # Botón para cerrar sesión
        boton_cerrar_sesion = tk.Button(marco_botones, text="Cerrar Sesión", font=("Arial", 12), bg="#FF0000", fg="white", command=lambda: cerrar_sesion(ventana_estudiante))
        boton_cerrar_sesion.pack(side="left", padx=5)

        # Crear Treeview para mostrar la tabla de información del estudiante sin la columna de privilegio
        tree_info = ttk.Treeview(ventana_estudiante, columns=("matricula", "grado", "grupo", "promedio", "modalidad", "carrera", "curp"), show='headings')

        # Definir los encabezados de las columnas
        tree_info.heading("matricula", text="Matrícula")
        tree_info.heading("grado", text="Grado")
        tree_info.heading("grupo", text="Grupo")
        tree_info.heading("promedio", text="Promedio")
        tree_info.heading("modalidad", text="Modalidad")
        tree_info.heading("carrera", text="Carrera")
        tree_info.heading("curp", text="CURP")

        # Ajustar el tamaño de las columnas
        tree_info.column("matricula", width=100)
        tree_info.column("grado", width=50)
        tree_info.column("grupo", width=50)
        tree_info.column("promedio", width=80)
        tree_info.column("modalidad", width=100)
        tree_info.column("carrera", width=100)
        tree_info.column("curp", width=150)

        # Insertar los datos en la tabla, excluyendo el privilegio
        try:
            # Usar la clase Estudiantes para obtener los datos del estudiante
            estudiante = Estudiantes.mostrar()
            for row in estudiante:
                if row[0] == matricula:  # Verificar que la matrícula coincida
                    tree_info.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[7]))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo recuperar la información del estudiante: {e}")

        tree_info.pack(expand=True, fill='both')

        # Crear segunda tabla para mostrar las calificaciones
        tree_calificaciones = ttk.Treeview(ventana_estudiante, columns=("id_calificacion", "calificacion", "observaciones", "clave_materia", "matricula_estudiante"), show='headings')

        # Definir los encabezados de las columnas
        tree_calificaciones.heading("id_calificacion", text="ID Calificación")
        tree_calificaciones.heading("calificacion", text="Calificación")
        tree_calificaciones.heading("observaciones", text="Observaciones")
        tree_calificaciones.heading("clave_materia", text="Clave Materia")
        tree_calificaciones.heading("matricula_estudiante", text="Matrícula Estudiante")

        # Ajustar el tamaño de las columnas
        tree_calificaciones.column("id_calificacion", width=100)
        tree_calificaciones.column("calificacion", width=100)
        tree_calificaciones.column("observaciones", width=200)
        tree_calificaciones.column("clave_materia", width=100)
        tree_calificaciones.column("matricula_estudiante", width=150)

        # Insertar los datos de las calificaciones en la tabla
        try:
            # Usar la clase Calificaciones para obtener las calificaciones del estudiante por matrícula
            calificaciones = Calificaciones.consultar_por_matricula(matricula)
            for row in calificaciones:
                tree_calificaciones.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo recuperar las calificaciones: {e}")

        tree_calificaciones.pack(expand=True, fill='both', pady=10)

    def cambiar_contraseña():
        # Crear una nueva ventana para cambiar la contraseña
        ventana_cambiar_contraseña = tk.Toplevel()
        ventana_cambiar_contraseña.title("Cambiar Contraseña")
        ventana_cambiar_contraseña.geometry("400x200")

        # Etiqueta para la nueva contraseña
        etiqueta_nueva_contraseña = tk.Label(ventana_cambiar_contraseña, text="Nueva Contraseña:", font=("Arial", 12))
        etiqueta_nueva_contraseña.pack(pady=10)

        # Campo de entrada para la nueva contraseña
        entrada_nueva_contraseña = tk.Entry(ventana_cambiar_contraseña, font=("Arial", 12), show="*")
        entrada_nueva_contraseña.pack(pady=10)

        # Botón para confirmar el cambio de contraseña
        boton_confirmar = tk.Button(ventana_cambiar_contraseña, text="Confirmar", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: actualizar_contraseña(entrada_nueva_contraseña.get(), ventana_cambiar_contraseña))
        boton_confirmar.pack(pady=10)

    def actualizar_contraseña(nueva_contraseña, ventana_cambiar_contraseña):
        if not nueva_contraseña:
            messagebox.showerror("Error", "La contraseña no puede estar vacía.")
            return

        try:
            global curp_global  # Declarar la variable global para su uso aquí
            query = "UPDATE personas SET contrasena_persona = %s WHERE CURP_persona = %s"
            cursor.execute(query, (nueva_contraseña, curp_global))
            conexion.commit()

            messagebox.showinfo("Éxito", "Contraseña actualizada correctamente.")
            ventana_cambiar_contraseña.destroy()  # Cierra la ventana de cambiar contraseña

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar la contraseña: {e}")
        
    def cerrar_sesion(ventana_actual):
        ventana_actual.destroy()  # Cierra la ventana actual
        ventana.deiconify()  # Muestra nuevamente la ventana de inicio de sesión



    def abrir_menu_profesor(nombre_usuario):
        ventana.withdraw()  # Oculta la ventana de inicio de sesión
        ventana_profesor = tk.Toplevel()
        ventana_profesor.title("Menú Profesor")
        ventana_profesor.geometry("900x700")

        # Etiqueta de bienvenida en la parte superior izquierda
        etiqueta_bienvenida = tk.Label(ventana_profesor, text=f"Bienvenido, {nombre_usuario}", font=("Arial", 14, "bold"))
        etiqueta_bienvenida.pack(anchor="nw", padx=10, pady=10)

        # Frame para los botones de cambiar contraseña y cerrar sesión
        marco_botones = tk.Frame(ventana_profesor)
        marco_botones.pack(anchor="nw", padx=10, pady=(0, 10))

        # Botón para cambiar contraseña
        boton_cambiar_contraseña = tk.Button(marco_botones, text="Cambiar Contraseña", font=("Arial", 12), bg="#4CAF50", fg="white", command=cambiar_contraseña)
        boton_cambiar_contraseña.pack(side="left", padx=5)

        # Botón para cerrar sesión
        boton_cerrar_sesion = tk.Button(marco_botones, text="Cerrar Sesión", font=("Arial", 12), bg="#FF0000", fg="white", command=lambda: cerrar_sesion(ventana_profesor))
        boton_cerrar_sesion.pack(side="left", padx=5)

        # Crear Treeview para mostrar todos los estudiantes
        tree_estudiantes = ttk.Treeview(ventana_profesor, columns=("matricula", "grado", "grupo", "promedio", "modalidad", "carrera", "curp"), show='headings')

        # Definir los encabezados de las columnas
        tree_estudiantes.heading("matricula", text="Matrícula")
        tree_estudiantes.heading("grado", text="Grado")
        tree_estudiantes.heading("grupo", text="Grupo")
        tree_estudiantes.heading("promedio", text="Promedio")
        tree_estudiantes.heading("modalidad", text="Modalidad")
        tree_estudiantes.heading("carrera", text="Carrera")
        tree_estudiantes.heading("curp", text="CURP")

        # Ajustar el tamaño de las columnas
        tree_estudiantes.column("matricula", width=100)
        tree_estudiantes.column("grado", width=50)
        tree_estudiantes.column("grupo", width=50)
        tree_estudiantes.column("promedio", width=80)
        tree_estudiantes.column("modalidad", width=100)
        tree_estudiantes.column("carrera", width=100)
        tree_estudiantes.column("curp", width=150)

        # Insertar los datos en la tabla
        try:
            # Usar la clase Estudiantes para obtener todos los estudiantes
            estudiantes = Estudiantes.mostrar()
            for row in estudiantes:
                tree_estudiantes.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[7]))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo recuperar la información de los estudiantes: {e}")

        tree_estudiantes.pack(expand=True, fill='both')

        # Crear segunda tabla para mostrar todas las calificaciones
        tree_calificaciones = ttk.Treeview(ventana_profesor, columns=("id_calificacion", "calificacion", "observaciones", "clave_materia", "matricula_estudiante"), show='headings')

        # Definir los encabezados de las columnas
        tree_calificaciones.heading("id_calificacion", text="ID Calificación")
        tree_calificaciones.heading("calificacion", text="Calificación")
        tree_calificaciones.heading("observaciones", text="Observaciones")
        tree_calificaciones.heading("clave_materia", text="Clave Materia")
        tree_calificaciones.heading("matricula_estudiante", text="Matrícula Estudiante")

        # Ajustar el tamaño de las columnas
        tree_calificaciones.column("id_calificacion", width=100)
        tree_calificaciones.column("calificacion", width=100)
        tree_calificaciones.column("observaciones", width=200)
        tree_calificaciones.column("clave_materia", width=100)
        tree_calificaciones.column("matricula_estudiante", width=150)

        # Insertar los datos de las calificaciones en la tabla
        try:
            # Usar la clase Calificaciones para obtener todas las calificaciones
            calificaciones = Calificaciones.mostrar()
            for row in calificaciones:
                tree_calificaciones.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo recuperar las calificaciones: {e}")

        tree_calificaciones.pack(expand=True, fill='both', pady=10)

        # Botones para ingresar y modificar calificaciones
        marco_botones = tk.Frame(ventana_profesor)
        marco_botones.pack(pady=10)

        boton_ingresar = tk.Button(marco_botones, text="Ingresar Calificaciones", font=("Arial", 12), bg="#4CAF50", fg="white", command=ingresar_calificaciones)
        boton_ingresar.grid(row=0, column=0, padx=10)

        boton_modificar = tk.Button(marco_botones, text="Modificar Calificaciones", font=("Arial", 12), bg="#FF9800", fg="white", command=modificar_calificaciones)
        boton_modificar.grid(row=0, column=1, padx=10)


    def abrir_menu_administrador(nombre_usuario):
        ventana.withdraw()  # Oculta la ventana de inicio de sesión
        ventana_administrador = tk.Toplevel()
        ventana_administrador.title("Menú Administrador")
        ventana_administrador.geometry("900x700")

        # Etiqueta de bienvenida en la parte superior izquierda
        etiqueta_bienvenida = tk.Label(ventana_administrador, text=f"Bienvenido, {nombre_usuario}", font=("Arial", 14, "bold"))
        etiqueta_bienvenida.pack(anchor="nw", padx=10, pady=10)

        # Frame para los botones de cambiar contraseña, cerrar sesión, agregar personas y modificar personas
        marco_botones = tk.Frame(ventana_administrador)
        marco_botones.pack(anchor="nw", padx=10, pady=(0, 10))

        # Botón para cambiar contraseña
        boton_cambiar_contraseña = tk.Button(marco_botones, text="Cambiar Contraseña", font=("Arial", 12), bg="#4CAF50", fg="white", command=cambiar_contraseña)
        boton_cambiar_contraseña.pack(side="left", padx=5)

        # Botón para cerrar sesión
        boton_cerrar_sesion = tk.Button(marco_botones, text="Cerrar Sesión", font=("Arial", 12), bg="#FF0000", fg="white", command=lambda: cerrar_sesion(ventana_administrador))
        boton_cerrar_sesion.pack(side="left", padx=5)

        # Botón para agregar personas
        boton_agregar_personas = tk.Button(marco_botones, text="Agregar Personas", font=("Arial", 12), bg="#4CAF50", fg="white", command=agregar_personas)
        boton_agregar_personas.pack(side="left", padx=5)

        # Botón para modificar personas
        boton_modificar_personas = tk.Button(marco_botones, text="Modificar Personas", font=("Arial", 12), bg="#FF9800", fg="white", command=modificar_personas)
        boton_modificar_personas.pack(side="left", padx=5)

        # Crear Treeview para mostrar todos los estudiantes
        tree_estudiantes = ttk.Treeview(ventana_administrador, columns=("matricula", "grado", "grupo", "promedio", "carrera", "privilegio", "curp"), show='headings')

        # Definir los encabezados de las columnas para estudiantes
        tree_estudiantes.heading("matricula", text="Matrícula")
        tree_estudiantes.heading("grado", text="Grado")
        tree_estudiantes.heading("grupo", text="Grupo")
        tree_estudiantes.heading("promedio", text="Promedio")
        tree_estudiantes.heading("carrera", text="Carrera")
        tree_estudiantes.heading("privilegio", text="Privilegio")
        tree_estudiantes.heading("curp", text="CURP")

        # Ajustar el tamaño de las columnas
        tree_estudiantes.column("matricula", width=100)
        tree_estudiantes.column("grado", width=50)
        tree_estudiantes.column("grupo", width=50)
        tree_estudiantes.column("promedio", width=80)
        tree_estudiantes.column("carrera", width=100)
        tree_estudiantes.column("privilegio", width=100)
        tree_estudiantes.column("curp", width=150)

        # Insertar los datos en la tabla
        try:
            estudiantes = Estudiantes.mostrar()
            for row in estudiantes:
                tree_estudiantes.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[7]))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo recuperar la información de los estudiantes: {e}")

        tree_estudiantes.pack(expand=True, fill='both')

        # Crear Treeview para mostrar todos los profesores
        tree_profesores = ttk.Treeview(ventana_administrador, columns=("matricula", "puesto", "salario", "antiguedad", "titulo", "privilegio", "curp"), show='headings')

        # Definir los encabezados de las columnas para profesores
        tree_profesores.heading("matricula", text="Matrícula")
        tree_profesores.heading("puesto", text="Puesto")
        tree_profesores.heading("salario", text="Salario")
        tree_profesores.heading("antiguedad", text="Antigüedad")
        tree_profesores.heading("titulo", text="Título")
        tree_profesores.heading("privilegio", text="Privilegio")
        tree_profesores.heading("curp", text="CURP")

        # Ajustar el tamaño de las columnas
        tree_profesores.column("matricula", width=100)
        tree_profesores.column("puesto", width=100)
        tree_profesores.column("salario", width=100)
        tree_profesores.column("antiguedad", width=100)
        tree_profesores.column("titulo", width=100)
        tree_profesores.column("privilegio", width=100)
        tree_profesores.column("curp", width=150)

        # Insertar los datos en la tabla
        try:
            profesores = Profesores.mostrar()
            for row in profesores:
                tree_profesores.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo recuperar la información de los profesores: {e}")

        tree_profesores.pack(expand=True, fill='both', pady=10)

        # Botones para ingresar y modificar alumnos y maestros
        marco_botones_admin = tk.Frame(ventana_administrador)
        marco_botones_admin.pack(pady=10)

        boton_ingresar_alumnos = tk.Button(marco_botones_admin, text="Ingresar Alumnos", font=("Arial", 12), bg="#4CAF50", fg="white", command=ingresar_alumnos)
        boton_ingresar_alumnos.grid(row=0, column=0, padx=10)

        boton_modificar_alumnos = tk.Button(marco_botones_admin, text="Modificar Alumnos", font=("Arial", 12), bg="#FF9800", fg="white", command=modificar_alumnos)
        boton_modificar_alumnos.grid(row=0, column=1, padx=10)

        boton_ingresar_maestros = tk.Button(marco_botones_admin, text="Ingresar Maestros", font=("Arial", 12), bg="#4CAF50", fg="white", command=ingresar_maestros)
        boton_ingresar_maestros.grid(row=1, column=0, padx=10, pady=10)

        boton_modificar_maestros = tk.Button(marco_botones_admin, text="Modificar Maestros", font=("Arial", 12), bg="#FF9800", fg="white", command=modificar_maestros)
        boton_modificar_maestros.grid(row=1, column=1, padx=10, pady=10)

    def agregar_personas():
        ventana_agregar_personas = tk.Toplevel()
        ventana_agregar_personas.title("Agregar Personas")
        ventana_agregar_personas.geometry("400x600")

        # Crear un Canvas y un Frame dentro del Canvas
        canvas = tk.Canvas(ventana_agregar_personas)
        scroll_y = tk.Scrollbar(ventana_agregar_personas, orient="vertical", command=canvas.yview)
        frame_formulario = tk.Frame(canvas)

        # Configurar el Canvas y el Scrollbar
        canvas.configure(yscrollcommand=scroll_y.set)
        scroll_y.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=frame_formulario, anchor="nw")

        # Etiquetas y entradas para cada campo
        etiquetas = [
            "CURP", "Nombre", "Apellido Paterno", "Apellido Materno", 
            "Edad", "Teléfono", "Email", "Dirección", 
            "Contraseña", "Escuela"
        ]
        
        entradas = {}
        for i, etiqueta in enumerate(etiquetas):
            tk.Label(frame_formulario, text=etiqueta, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entradas[etiqueta] = tk.Entry(frame_formulario, font=("Arial", 12))
            entradas[etiqueta].grid(row=i, column=1, padx=10, pady=5)

        # Función para confirmar y guardar
        def confirmar_agregar():
            valores = {key: entrada.get() for key, entrada in entradas.items()}
            try:
                query = """
                    INSERT INTO personas (CURP_persona, nombre_persona, apellidop_persona, apellidom_persona, edad_persona, 
                                        telefono_persona, email_persona, direccion_persona, contrasena_persona, escuela_persona) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, tuple(valores.values()))
                conexion.commit()
                messagebox.showinfo("Éxito", "Persona agregada exitosamente")
                ventana_agregar_personas.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar la persona: {e}")

        # Botón de confirmar
        boton_confirmar = tk.Button(frame_formulario, text="Confirmar", font=("Arial", 12), bg="#4CAF50", fg="white", command=confirmar_agregar)
        boton_confirmar.grid(row=len(etiquetas), columnspan=2, pady=20)

        # Configuración del Scrollbar
        frame_formulario.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    def modificar_personas():
        ventana_modificar_personas = tk.Toplevel()
        ventana_modificar_personas.title("Modificar Personas")
        ventana_modificar_personas.geometry("400x600")

        # Crear un Canvas y un Frame dentro del Canvas
        canvas = tk.Canvas(ventana_modificar_personas)
        scroll_y = tk.Scrollbar(ventana_modificar_personas, orient="vertical", command=canvas.yview)
        frame_formulario = tk.Frame(canvas)

        # Configurar el Canvas y el Scrollbar
        canvas.configure(yscrollcommand=scroll_y.set)
        scroll_y.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=frame_formulario, anchor="nw")

        # Etiquetas y entradas para cada campo
        etiquetas = [
            "CURP", "Nombre", "Apellido Paterno", "Apellido Materno", 
            "Edad", "Teléfono", "Email", "Dirección", 
            "Contraseña", "Escuela"
        ]
        
        entradas = {}
        for i, etiqueta in enumerate(etiquetas):
            tk.Label(frame_formulario, text=etiqueta, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entradas[etiqueta] = tk.Entry(frame_formulario, font=("Arial", 12))
            entradas[etiqueta].grid(row=i, column=1, padx=10, pady=5)

        # Función para confirmar y modificar
        def confirmar_modificar():
            valores = {key: entrada.get() for key, entrada in entradas.items()}
            try:
                query = """
                    UPDATE personas SET nombre_persona=%s, apellidop_persona=%s, apellidom_persona=%s, edad_persona=%s, 
                                        telefono_persona=%s, email_persona=%s, direccion_persona=%s, contrasena_persona=%s, 
                                        escuela_persona=%s WHERE CURP_persona=%s
                """
                cursor.execute(query, (
                    valores["Nombre"], valores["Apellido Paterno"], valores["Apellido Materno"], valores["Edad"], 
                    valores["Teléfono"], valores["Email"], valores["Dirección"], valores["Contraseña"], valores["Escuela"], valores["CURP"]
                ))
                conexion.commit()
                messagebox.showinfo("Éxito", "Persona modificada exitosamente")
                ventana_modificar_personas.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo modificar la persona: {e}")

        # Botón de confirmar
        boton_confirmar = tk.Button(frame_formulario, text="Modificar", font=("Arial", 12), bg="#FF9800", fg="white", command=confirmar_modificar)
        boton_confirmar.grid(row=len(etiquetas), columnspan=2, pady=20)

        # Configuración del Scrollbar
        frame_formulario.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    def ingresar_alumnos():
        # Crear una nueva ventana para ingresar alumnos
        ventana_ingresar_alumnos = tk.Toplevel()
        ventana_ingresar_alumnos.title("Ingresar Alumnos")
        ventana_ingresar_alumnos.geometry("400x400")

        # Etiquetas y campos de entrada para la tabla estudiantes
        # Primero se debe haber ingresado la persona correspondiente en la tabla personas
        etiqueta_matricula = tk.Label(ventana_ingresar_alumnos, text="Matrícula Estudiante:", font=("Arial", 12))
        etiqueta_matricula.pack(pady=10)
        entrada_matricula = tk.Entry(ventana_ingresar_alumnos, font=("Arial", 12))
        entrada_matricula.pack(pady=5)

        etiqueta_grado = tk.Label(ventana_ingresar_alumnos, text="Grado Estudiante:", font=("Arial", 12))
        etiqueta_grado.pack(pady=10)
        entrada_grado = tk.Entry(ventana_ingresar_alumnos, font=("Arial", 12))
        entrada_grado.pack(pady=5)

        etiqueta_grupo = tk.Label(ventana_ingresar_alumnos, text="Grupo Estudiante:", font=("Arial", 12))
        etiqueta_grupo.pack(pady=10)
        entrada_grupo = tk.Entry(ventana_ingresar_alumnos, font=("Arial", 12))
        entrada_grupo.pack(pady=5)

        etiqueta_promedio = tk.Label(ventana_ingresar_alumnos, text="Promedio Estudiante:", font=("Arial", 12))
        etiqueta_promedio.pack(pady=10)
        entrada_promedio = tk.Entry(ventana_ingresar_alumnos, font=("Arial", 12))
        entrada_promedio.pack(pady=5)

        etiqueta_carrera = tk.Label(ventana_ingresar_alumnos, text="Carrera Estudiante:", font=("Arial", 12))
        etiqueta_carrera.pack(pady=10)
        entrada_carrera = tk.Entry(ventana_ingresar_alumnos, font=("Arial", 12))
        entrada_carrera.pack(pady=5)

        etiqueta_curp = tk.Label(ventana_ingresar_alumnos, text="CURP Estudiante:", font=("Arial", 12))
        etiqueta_curp.pack(pady=10)
        entrada_curp = tk.Entry(ventana_ingresar_alumnos, font=("Arial", 12))
        entrada_curp.pack(pady=5)

        boton_confirmar = tk.Button(ventana_ingresar_alumnos, text="Confirmar", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: guardar_alumno(
            entrada_matricula.get(), entrada_grado.get(), entrada_grupo.get(), entrada_promedio.get(), entrada_carrera.get(), entrada_curp.get(), ventana_ingresar_alumnos))
        boton_confirmar.pack(pady=20)


    def guardar_alumno(matricula, grado, grupo, promedio, carrera, curp, ventana_ingresar_alumnos):
        if not matricula or not curp:
            messagebox.showerror("Error", "Los campos de matrícula y CURP son obligatorios.")
            return

        try:
            query_insert = """
                INSERT INTO estudiantes (matricula_estudiante, grado_estudiante, grupo_estudiante, promedio_estudiante, carrera_estudiante, CURP_persona) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query_insert, (matricula, grado, grupo, promedio, carrera, curp))
            conexion.commit()

            messagebox.showinfo("Éxito", "Alumno ingresado correctamente.")
            ventana_ingresar_alumnos.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo ingresar el alumno: {e}")


    def ingresar_maestros():
        # Crear una nueva ventana para ingresar maestros
        ventana_ingresar_maestros = tk.Toplevel()
        ventana_ingresar_maestros.title("Ingresar Maestros")
        ventana_ingresar_maestros.geometry("400x400")

        # Etiquetas y campos de entrada para la tabla profesores
        etiqueta_matricula = tk.Label(ventana_ingresar_maestros, text="Matrícula Profesor:", font=("Arial", 12))
        etiqueta_matricula.pack(pady=10)
        entrada_matricula = tk.Entry(ventana_ingresar_maestros, font=("Arial", 12))
        entrada_matricula.pack(pady=5)

        etiqueta_puesto = tk.Label(ventana_ingresar_maestros, text="Puesto Profesor:", font=("Arial", 12))
        etiqueta_puesto.pack(pady=10)
        entrada_puesto = tk.Entry(ventana_ingresar_maestros, font=("Arial", 12))
        entrada_puesto.pack(pady=5)

        etiqueta_salario = tk.Label(ventana_ingresar_maestros, text="Salario Profesor:", font=("Arial", 12))
        etiqueta_salario.pack(pady=10)
        entrada_salario = tk.Entry(ventana_ingresar_maestros, font=("Arial", 12))
        entrada_salario.pack(pady=5)

        etiqueta_antiguedad = tk.Label(ventana_ingresar_maestros, text="Antigüedad Profesor:", font=("Arial", 12))
        etiqueta_antiguedad.pack(pady=10)
        entrada_antiguedad = tk.Entry(ventana_ingresar_maestros, font=("Arial", 12))
        entrada_antiguedad.pack(pady=5)

        etiqueta_titulo = tk.Label(ventana_ingresar_maestros, text="Título Profesor:", font=("Arial", 12))
        etiqueta_titulo.pack(pady=10)
        entrada_titulo = tk.Entry(ventana_ingresar_maestros, font=("Arial", 12))
        entrada_titulo.pack(pady=5)

        etiqueta_curp = tk.Label(ventana_ingresar_maestros, text="CURP Profesor:", font=("Arial", 12))
        etiqueta_curp.pack(pady=10)
        entrada_curp = tk.Entry(ventana_ingresar_maestros, font=("Arial", 12))
        entrada_curp.pack(pady=5)

        boton_confirmar = tk.Button(ventana_ingresar_maestros, text="Confirmar", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: guardar_maestro(
            entrada_matricula.get(), entrada_puesto.get(), entrada_salario.get(), entrada_antiguedad.get(), entrada_titulo.get(), entrada_curp.get(), ventana_ingresar_maestros))
        boton_confirmar.pack(pady=20)


    def guardar_maestro(matricula, puesto, salario, antiguedad, titulo, curp, ventana_ingresar_maestros):
        if not matricula or not curp:
            messagebox.showerror("Error", "Los campos de matrícula y CURP son obligatorios.")
            return

        try:
            query_insert = """
                INSERT INTO profesores (matricula_profesor, puesto_profesor, salario_profesor, antiguedad_profesor, titulo_profesor, CURP_persona) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query_insert, (matricula, puesto, salario, antiguedad, titulo, curp))
            conexion.commit()

            messagebox.showinfo("Éxito", "Maestro ingresado correctamente.")
            ventana_ingresar_maestros.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo ingresar el maestro: {e}")

    def modificar_alumnos():
        # Crear una nueva ventana para modificar alumnos
        ventana_modificar_alumnos = tk.Toplevel()
        ventana_modificar_alumnos.title("Modificar Alumnos")
        ventana_modificar_alumnos.geometry("400x500")

        # Etiqueta y campo de entrada para la matrícula del estudiante
        etiqueta_matricula = tk.Label(ventana_modificar_alumnos, text="Matrícula Estudiante:", font=("Arial", 12))
        etiqueta_matricula.pack(pady=10)
        entrada_matricula = tk.Entry(ventana_modificar_alumnos, font=("Arial", 12))
        entrada_matricula.pack(pady=5)

        # Etiqueta y campo de entrada para el nuevo grado del estudiante
        etiqueta_nuevo_grado = tk.Label(ventana_modificar_alumnos, text="Nuevo Grado:", font=("Arial", 12))
        etiqueta_nuevo_grado.pack(pady=10)
        entrada_nuevo_grado = tk.Entry(ventana_modificar_alumnos, font=("Arial", 12))
        entrada_nuevo_grado.pack(pady=5)

        # Etiqueta y campo de entrada para el nuevo grupo del estudiante
        etiqueta_nuevo_grupo = tk.Label(ventana_modificar_alumnos, text="Nuevo Grupo:", font=("Arial", 12))
        etiqueta_nuevo_grupo.pack(pady=10)
        entrada_nuevo_grupo = tk.Entry(ventana_modificar_alumnos, font=("Arial", 12))
        entrada_nuevo_grupo.pack(pady=5)

        # Etiqueta y campo de entrada para el nuevo promedio del estudiante
        etiqueta_nuevo_promedio = tk.Label(ventana_modificar_alumnos, text="Nuevo Promedio:", font=("Arial", 12))
        etiqueta_nuevo_promedio.pack(pady=10)
        entrada_nuevo_promedio = tk.Entry(ventana_modificar_alumnos, font=("Arial", 12))
        entrada_nuevo_promedio.pack(pady=5)

        # Etiqueta y campo de entrada para la nueva carrera del estudiante
        etiqueta_nueva_carrera = tk.Label(ventana_modificar_alumnos, text="Nueva Carrera:", font=("Arial", 12))
        etiqueta_nueva_carrera.pack(pady=10)
        entrada_nueva_carrera = tk.Entry(ventana_modificar_alumnos, font=("Arial", 12))
        entrada_nueva_carrera.pack(pady=5)

        # Botón para confirmar la modificación del alumno
        boton_confirmar_modificacion = tk.Button(ventana_modificar_alumnos, text="Modificar", font=("Arial", 12), bg="#FF9800", fg="white", command=lambda: actualizar_alumno(
            entrada_matricula.get(),
            entrada_nuevo_grado.get(),
            entrada_nuevo_grupo.get(),
            entrada_nuevo_promedio.get(),
            entrada_nueva_carrera.get(),
            ventana_modificar_alumnos
        ))
        boton_confirmar_modificacion.pack(pady=20)

    def actualizar_alumno(matricula, nuevo_grado, nuevo_grupo, nuevo_promedio, nueva_carrera, ventana_modificar_alumnos):
        # Verificar que la matrícula esté llena
        if not matricula:
            messagebox.showerror("Error", "La matrícula es obligatoria.")
            return

        try:
            # Verificar que el alumno con la matrícula dada existe
            query_verificar_alumno = "SELECT COUNT(*) FROM estudiantes WHERE matricula_estudiante = %s"
            cursor.execute(query_verificar_alumno, (matricula,))
            if cursor.fetchone()[0] == 0:
                messagebox.showerror("Error", "El alumno con la matrícula proporcionada no existe.")
                return

            # Construir la consulta de actualización dinámica
            campos_a_modificar = []
            valores = []

            if nuevo_grado:
                campos_a_modificar.append("grado_estudiante = %s")
                valores.append(nuevo_grado)
            if nuevo_grupo:
                campos_a_modificar.append("grupo_estudiante = %s")
                valores.append(nuevo_grupo)
            if nuevo_promedio:
                campos_a_modificar.append("promedio_estudiante = %s")
                valores.append(nuevo_promedio)
            if nueva_carrera:
                campos_a_modificar.append("carrera_estudiante = %s")
                valores.append(nueva_carrera)

            # Si no hay cambios, no realizar la actualización
            if not campos_a_modificar:
                messagebox.showerror("Error", "No se proporcionaron cambios para actualizar.")
                return

            # Agregar la matrícula del estudiante para la cláusula WHERE
            valores.append(matricula)

            query_actualizar = f"UPDATE estudiantes SET {', '.join(campos_a_modificar)} WHERE matricula_estudiante = %s"
            cursor.execute(query_actualizar, valores)
            conexion.commit()

            messagebox.showinfo("Éxito", "Alumno modificado correctamente.")
            ventana_modificar_alumnos.destroy()  # Cierra la ventana de modificación de alumnos

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo modificar el alumno: {e}")



    def modificar_maestros():
        # Crear una nueva ventana para modificar maestros
        ventana_modificar_maestros = tk.Toplevel()
        ventana_modificar_maestros.title("Modificar Maestros")
        ventana_modificar_maestros.geometry("400x500")

        # Etiqueta y campo de entrada para la matrícula del profesor
        etiqueta_matricula = tk.Label(ventana_modificar_maestros, text="Matrícula Profesor:", font=("Arial", 12))
        etiqueta_matricula.pack(pady=10)
        entrada_matricula = tk.Entry(ventana_modificar_maestros, font=("Arial", 12))
        entrada_matricula.pack(pady=5)

        # Etiqueta y campo de entrada para el nuevo puesto del profesor
        etiqueta_nuevo_puesto = tk.Label(ventana_modificar_maestros, text="Nuevo Puesto:", font=("Arial", 12))
        etiqueta_nuevo_puesto.pack(pady=10)
        entrada_nuevo_puesto = tk.Entry(ventana_modificar_maestros, font=("Arial", 12))
        entrada_nuevo_puesto.pack(pady=5)

        # Etiqueta y campo de entrada para el nuevo salario del profesor
        etiqueta_nuevo_salario = tk.Label(ventana_modificar_maestros, text="Nuevo Salario:", font=("Arial", 12))
        etiqueta_nuevo_salario.pack(pady=10)
        entrada_nuevo_salario = tk.Entry(ventana_modificar_maestros, font=("Arial", 12))
        entrada_nuevo_salario.pack(pady=5)

        # Etiqueta y campo de entrada para la nueva antigüedad del profesor
        etiqueta_nueva_antiguedad = tk.Label(ventana_modificar_maestros, text="Nueva Antigüedad:", font=("Arial", 12))
        etiqueta_nueva_antiguedad.pack(pady=10)
        entrada_nueva_antiguedad = tk.Entry(ventana_modificar_maestros, font=("Arial", 12))
        entrada_nueva_antiguedad.pack(pady=5)

        # Etiqueta y campo de entrada para el nuevo título del profesor
        etiqueta_nuevo_titulo = tk.Label(ventana_modificar_maestros, text="Nuevo Título:", font=("Arial", 12))
        etiqueta_nuevo_titulo.pack(pady=10)
        entrada_nuevo_titulo = tk.Entry(ventana_modificar_maestros, font=("Arial", 12))
        entrada_nuevo_titulo.pack(pady=5)

        # Botón para confirmar la modificación del maestro
        boton_confirmar_modificacion = tk.Button(ventana_modificar_maestros, text="Modificar", font=("Arial", 12), bg="#FF9800", fg="white", command=lambda: actualizar_maestro(
            entrada_matricula.get(),
            entrada_nuevo_puesto.get(),
            entrada_nuevo_salario.get(),
            entrada_nueva_antiguedad.get(),
            entrada_nuevo_titulo.get(),
            ventana_modificar_maestros
        ))
        boton_confirmar_modificacion.pack(pady=20)

    def actualizar_maestro(matricula, nuevo_puesto, nuevo_salario, nueva_antiguedad, nuevo_titulo, ventana_modificar_maestros):
        # Verificar que la matrícula esté llena
        if not matricula:
            messagebox.showerror("Error", "La matrícula es obligatoria.")
            return

        try:
            # Verificar que el maestro con la matrícula dada existe
            query_verificar_maestro = "SELECT COUNT(*) FROM profesores WHERE matricula_profesor = %s"
            cursor.execute(query_verificar_maestro, (matricula,))
            if cursor.fetchone()[0] == 0:
                messagebox.showerror("Error", "El maestro con la matrícula proporcionada no existe.")
                return

            # Construir la consulta de actualización dinámica
            campos_a_modificar = []
            valores = []

            if nuevo_puesto:
                campos_a_modificar.append("puesto_profesor = %s")
                valores.append(nuevo_puesto)
            if nuevo_salario:
                campos_a_modificar.append("salario_profesor = %s")
                valores.append(nuevo_salario)
            if nueva_antiguedad:
                campos_a_modificar.append("antiguedad_profesor = %s")
                valores.append(nueva_antiguedad)
            if nuevo_titulo:
                campos_a_modificar.append("titulo_profesor = %s")
                valores.append(nuevo_titulo)

            # Si no hay cambios, no realizar la actualización
            if not campos_a_modificar:
                messagebox.showerror("Error", "No se proporcionaron cambios para actualizar.")
                return

            # Agregar la matrícula del profesor para la cláusula WHERE
            valores.append(matricula)

            query_actualizar = f"UPDATE profesores SET {', '.join(campos_a_modificar)} WHERE matricula_profesor = %s"
            cursor.execute(query_actualizar, valores)
            conexion.commit()

            messagebox.showinfo("Éxito", "Maestro modificado correctamente.")
            ventana_modificar_maestros.destroy()  # Cierra la ventana de modificación de maestros

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo modificar el maestro: {e}")



    def ingresar_calificaciones():
        # Crear una nueva ventana para ingresar las calificaciones
        ventana_ingresar_calificaciones = tk.Toplevel()
        ventana_ingresar_calificaciones.title("Ingresar Calificaciones")
        ventana_ingresar_calificaciones.geometry("400x400")

        # Etiqueta y campo de entrada para la calificación
        etiqueta_calificacion = tk.Label(ventana_ingresar_calificaciones, text="Calificación:", font=("Arial", 12))
        etiqueta_calificacion.pack(pady=10)
        entrada_calificacion = tk.Entry(ventana_ingresar_calificaciones, font=("Arial", 12))
        entrada_calificacion.pack(pady=5)

        # Etiqueta y campo de entrada para las observaciones
        etiqueta_observaciones = tk.Label(ventana_ingresar_calificaciones, text="Observaciones:", font=("Arial", 12))
        etiqueta_observaciones.pack(pady=10)
        entrada_observaciones = tk.Entry(ventana_ingresar_calificaciones, font=("Arial", 12))
        entrada_observaciones.pack(pady=5)

        # Etiqueta y campo de entrada para la clave de la materia
        etiqueta_clave_materia = tk.Label(ventana_ingresar_calificaciones, text="Clave Materia:", font=("Arial", 12))
        etiqueta_clave_materia.pack(pady=10)
        entrada_clave_materia = tk.Entry(ventana_ingresar_calificaciones, font=("Arial", 12))
        entrada_clave_materia.pack(pady=5)

        # Etiqueta y campo de entrada para la matrícula del estudiante
        etiqueta_matricula_estudiante = tk.Label(ventana_ingresar_calificaciones, text="Matrícula Estudiante:", font=("Arial", 12))
        etiqueta_matricula_estudiante.pack(pady=10)
        entrada_matricula_estudiante = tk.Entry(ventana_ingresar_calificaciones, font=("Arial", 12))
        entrada_matricula_estudiante.pack(pady=5)

        # Botón para confirmar el ingreso de la calificación
        boton_confirmar = tk.Button(ventana_ingresar_calificaciones, text="Confirmar", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: guardar_calificacion(
            entrada_calificacion.get(),
            entrada_observaciones.get(),
            entrada_clave_materia.get(),
            entrada_matricula_estudiante.get(),
            ventana_ingresar_calificaciones
        ))
        boton_confirmar.pack(pady=20)

    def guardar_calificacion(calificacion, observaciones, clave_materia, matricula_estudiante, ventana_ingresar_calificaciones):
        # Verificar que todos los campos estén llenos
        if not calificacion or not clave_materia or not matricula_estudiante:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        try:
            # Verificar que la clave de la materia exista
            query_materia = "SELECT COUNT(*) FROM materias WHERE clave_materia = %s"
            cursor.execute(query_materia, (clave_materia,))
            if cursor.fetchone()[0] == 0:
                messagebox.showerror("Error", "La clave de la materia no existe.")
                return
            
            # Verificar que la matrícula del estudiante exista
            query_estudiante = "SELECT COUNT(*) FROM estudiantes WHERE matricula_estudiante = %s"
            cursor.execute(query_estudiante, (matricula_estudiante,))
            if cursor.fetchone()[0] == 0:
                messagebox.showerror("Error", "La matrícula del estudiante no existe.")
                return
            
            # Insertar la nueva calificación
            query_insert = """
                INSERT INTO calificaciones (calificacion, observaciones, clave_materia, matricula_estudiante) 
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query_insert, (calificacion, observaciones, clave_materia, matricula_estudiante))
            conexion.commit()

            messagebox.showinfo("Éxito", "Calificación ingresada correctamente.")
            ventana_ingresar_calificaciones.destroy()  # Cierra la ventana de ingreso de calificaciones

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo ingresar la calificación: {e}")


    def modificar_calificaciones():
        # Crear una nueva ventana para modificar las calificaciones
        ventana_modificar_calificaciones = tk.Toplevel()
        ventana_modificar_calificaciones.title("Modificar Calificaciones")
        ventana_modificar_calificaciones.geometry("400x500")

        # Etiqueta y campo de entrada para el ID de la calificación
        etiqueta_id_calificacion = tk.Label(ventana_modificar_calificaciones, text="ID Calificación:", font=("Arial", 12))
        etiqueta_id_calificacion.pack(pady=10)
        entrada_id_calificacion = tk.Entry(ventana_modificar_calificaciones, font=("Arial", 12))
        entrada_id_calificacion.pack(pady=5)

        # Etiqueta y campo de entrada para la nueva calificación
        etiqueta_nueva_calificacion = tk.Label(ventana_modificar_calificaciones, text="Nueva Calificación:", font=("Arial", 12))
        etiqueta_nueva_calificacion.pack(pady=10)
        entrada_nueva_calificacion = tk.Entry(ventana_modificar_calificaciones, font=("Arial", 12))
        entrada_nueva_calificacion.pack(pady=5)

        # Etiqueta y campo de entrada para las nuevas observaciones
        etiqueta_nuevas_observaciones = tk.Label(ventana_modificar_calificaciones, text="Nuevas Observaciones:", font=("Arial", 12))
        etiqueta_nuevas_observaciones.pack(pady=10)
        entrada_nuevas_observaciones = tk.Entry(ventana_modificar_calificaciones, font=("Arial", 12))
        entrada_nuevas_observaciones.pack(pady=5)

        # Etiqueta y campo de entrada para la nueva clave de materia
        etiqueta_nueva_clave_materia = tk.Label(ventana_modificar_calificaciones, text="Nueva Clave Materia:", font=("Arial", 12))
        etiqueta_nueva_clave_materia.pack(pady=10)
        entrada_nueva_clave_materia = tk.Entry(ventana_modificar_calificaciones, font=("Arial", 12))
        entrada_nueva_clave_materia.pack(pady=5)

        # Etiqueta y campo de entrada para la nueva matrícula del estudiante
        etiqueta_nueva_matricula_estudiante = tk.Label(ventana_modificar_calificaciones, text="Nueva Matrícula Estudiante:", font=("Arial", 12))
        etiqueta_nueva_matricula_estudiante.pack(pady=10)
        entrada_nueva_matricula_estudiante = tk.Entry(ventana_modificar_calificaciones, font=("Arial", 12))
        entrada_nueva_matricula_estudiante.pack(pady=5)

        # Botón para confirmar la modificación de la calificación
        boton_confirmar_modificacion = tk.Button(ventana_modificar_calificaciones, text="Modificar", font=("Arial", 12), bg="#FF9800", fg="white", command=lambda: actualizar_calificacion(
            entrada_id_calificacion.get(),
            entrada_nueva_calificacion.get(),
            entrada_nuevas_observaciones.get(),
            entrada_nueva_clave_materia.get(),
            entrada_nueva_matricula_estudiante.get(),
            ventana_modificar_calificaciones
        ))
        boton_confirmar_modificacion.pack(pady=20)

    def actualizar_calificacion(id_calificacion, nueva_calificacion, nuevas_observaciones, nueva_clave_materia, nueva_matricula_estudiante, ventana_modificar_calificaciones):
        # Verificar que todos los campos estén llenos
        if not id_calificacion:
            messagebox.showerror("Error", "El ID de la calificación es obligatorio.")
            return

        try:
            # Verificar que la calificación con el ID dado existe
            query_verificar_calificacion = "SELECT COUNT(*) FROM calificaciones WHERE id_calificacion = %s"
            cursor.execute(query_verificar_calificacion, (id_calificacion,))
            if cursor.fetchone()[0] == 0:
                messagebox.showerror("Error", "La calificación con el ID proporcionado no existe.")
                return

            # Verificar que la clave de la materia exista si se proporciona una nueva clave
            if nueva_clave_materia:
                query_materia = "SELECT COUNT(*) FROM materias WHERE clave_materia = %s"
                cursor.execute(query_materia, (nueva_clave_materia,))
                if cursor.fetchone()[0] == 0:
                    messagebox.showerror("Error", "La clave de la materia no existe.")
                    return

            # Verificar que la matrícula del estudiante exista si se proporciona una nueva matrícula
            if nueva_matricula_estudiante:
                query_estudiante = "SELECT COUNT(*) FROM estudiantes WHERE matricula_estudiante = %s"
                cursor.execute(query_estudiante, (nueva_matricula_estudiante,))
                if cursor.fetchone()[0] == 0:
                    messagebox.showerror("Error", "La matrícula del estudiante no existe.")
                    return

            # Construir la consulta de actualización dinámica
            campos_a_modificar = []
            valores = []

            if nueva_calificacion:
                campos_a_modificar.append("calificacion = %s")
                valores.append(nueva_calificacion)
            if nuevas_observaciones:
                campos_a_modificar.append("observaciones = %s")
                valores.append(nuevas_observaciones)
            if nueva_clave_materia:
                campos_a_modificar.append("clave_materia = %s")
                valores.append(nueva_clave_materia)
            if nueva_matricula_estudiante:
                campos_a_modificar.append("matricula_estudiante = %s")
                valores.append(nueva_matricula_estudiante)

            # Si no hay cambios, no realizar la actualización
            if not campos_a_modificar:
                messagebox.showerror("Error", "No se proporcionaron cambios para actualizar.")
                return

            # Agregar el ID de la calificación para la cláusula WHERE
            valores.append(id_calificacion)

            query_actualizar = f"UPDATE calificaciones SET {', '.join(campos_a_modificar)} WHERE id_calificacion = %s"
            cursor.execute(query_actualizar, valores)
            conexion.commit()

            messagebox.showinfo("Éxito", "Calificación modificada correctamente.")
            ventana_modificar_calificaciones.destroy()  # Cierra la ventana de modificación de calificaciones

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo modificar la calificación: {e}")

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Formulario de inicio de sesión")
    ventana.geometry("900x600")
    ventana.configure(bg='#6A1B9A')

    # Crear un marco para el formulario
    marco_formulario = tk.Frame(ventana, bg="white", padx=80, pady=80)
    marco_formulario.place(relx=0.5, rely=0.5, anchor="center")

    # Etiqueta de título
    etiqueta_titulo = tk.Label(marco_formulario, text="Iniciar sesión", font=("Arial", 18, "bold"), bg="white", fg="black")
    etiqueta_titulo.pack(pady=(10, 20))

    # Etiqueta y entrada de correo
    etiqueta_correo = tk.Label(marco_formulario, text="Correo electrónico", font=("Arial", 12), bg="white", fg="black")
    etiqueta_correo.pack(anchor="w")
    entrada_correo = tk.Entry(marco_formulario, font=("Arial", 12), bd=2, relief="solid")
    entrada_correo.pack(fill="x", pady=(0, 10))

    # Etiqueta y entrada de contraseña
    etiqueta_contraseña = tk.Label(marco_formulario, text="Contraseña", font=("Arial", 12), bg="white", fg="black")
    entrada_contraseña = tk.Entry(marco_formulario, font=("Arial", 12), bd=2, relief="solid", show="*")
    etiqueta_contraseña.pack(anchor="w")
    entrada_contraseña.pack(fill="x", pady=(0, 20))

    # Botón de inicio de sesión
    boton_iniciar = tk.Button(marco_formulario, text="Ingresar", font=("Arial", 12, "bold"), bg="#FBC02D", fg="black", command=login)
    boton_iniciar.pack()

    ventana.mainloop()

if __name__ == "__main__":
    main()
