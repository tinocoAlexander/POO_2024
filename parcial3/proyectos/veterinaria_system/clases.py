from funciones import *
class Personas:
    def __init__(self, CURP_persona, nombre_persona, direccion_persona, telefono_persona, contrasena_persona):
        self.CURP_persona = CURP_persona
        self.nombre_persona = nombre_persona
        self.direccion_persona = direccion_persona
        self.telefono_persona = telefono_persona
        self.contrasena_persona = contrasena_persona
    
    def registrar_persona(self):
        cursor = conexion.cursor()
        # Consulta para insertar una persona en la tabla Personas
        consulta = "INSERT INTO Personas (CURP_persona, nombre_persona, direccion_persona, telefono_persona, contrasena_persona) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(consulta, (self.CURP_persona, self.nombre_persona, self.direccion_persona, self.telefono_persona, self.contrasena_persona))
        conexion.commit()
        return True, "Persona registrada correctamente."
    
    @staticmethod
    def mostrar_personas():
        cursor = conexion.cursor()
        # Consulta para mostrar las personas
        consulta = "SELECT * FROM Personas"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado
    
class Empleados: 
    def __init__(self, clave_empleado, puesto_empleado, salario_empleado, privilegio, CURP_persona):
        self.clave_empleado = clave_empleado
        self.puesto_empleado = puesto_empleado
        self.salario_empleado = salario_empleado
        self.privilegio = privilegio
        self.CURP_persona = CURP_persona
    
    def registrar_empleado(self):
        cursor = conexion.cursor()
        # Consulta para insertar un empleado en la tabla Empleados
        consulta = "INSERT INTO Empleados (clave_empleado, puesto_empleado, salario_empleado, privilegio, CURP_persona) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(consulta, (self.clave_empleado, self.puesto_empleado, self.salario_empleado, self.privilegio, self.CURP_persona))
        conexion.commit()
        return True, "Empleado registrado correctamente."
    

class Clientes:
    def __init__(self, clave_cliente, tipo_cliente, privilegio, CURP_persona):
        self.clave_cliente = clave_cliente
        self.tipo_cliente = tipo_cliente
        self.privilegio = privilegio
        self.CURP_persona = CURP_persona
    
    def registrar_cliente(self):
        cursor = conexion.cursor()
        # Consulta para insertar un cliente en la tabla Clientes
        consulta = "INSERT INTO Clientes (clave_cliente, tipo_cliente, privilegio, CURP_persona) VALUES (%s, %s, %s, %s)"
        cursor.execute(consulta, (self.clave_cliente, self.tipo_cliente, self.privilegio, self.CURP_persona))
        conexion.commit()
        return True, "Cliente registrado correctamente."
    
    

class Animales:
    def __init__(self, clave_animal, nombre_animal, raza_animal, edad_animal, clave_cliente):
        self.clave_animal = clave_animal
        self.nombre_animal = nombre_animal
        self.raza_animal = raza_animal
        self.edad_animal = edad_animal
        self.clave_cliente = clave_cliente

    def registrar_animal(self):
        cursor = conexion.cursor()
        # Consulta para insertar un animal en la tabla Animales
        consulta = "INSERT INTO Animales (clave_animal, nombre_animal, raza_animal, edad_animal, clave_cliente) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(consulta, (self.clave_animal, self.nombre_animal, self.raza_animal, self.edad_animal, self.clave_cliente))
        conexion.commit()
        return True, "Animal registrado correctamente."
    
    @staticmethod
    def actualizar_animal(clave_animal, nombre_animal, raza_animal, edad_animal):
        cursor = conexion.cursor()
        # Consulta para actualizar un animal en la tabla Animales
        consulta = "UPDATE Animales SET nombre_animal = %s, raza_animal = %s, edad_animal = %s WHERE clave_animal = %s"
        cursor.execute(consulta, (nombre_animal, raza_animal, edad_animal, clave_animal))
        conexion.commit()
        return True, "Animal actualizado correctamente."
    
    @staticmethod
    def eliminar_animal(clave_animal):
        cursor = conexion.cursor()
        # Consulta para eliminar un animal en la tabla Animales
        consulta = "DELETE FROM Animales WHERE clave_animal = %s"
        cursor.execute(consulta, (clave_animal,))
        conexion.commit()
        return True, "Animal eliminado correctamente."

class Consultas:
    def __init__(self, numero_consultas, clave_animal):
        self.numero_consultas = numero_consultas
        self.clave_animal = clave_animal
    
    def registrar_consulta(self):
        cursor = conexion.cursor()
        # Consulta para insertar una consulta en la tabla Consultas
        consulta = "INSERT INTO Consultas (numero_consultas, clave_animal) VALUES (%s, %s)"
        cursor.execute(consulta, (self.numero_consultas, self.clave_animal))
        conexion.commit()
        return True, "Consulta registrada correctamente."
    
    @staticmethod
    def mostrar_consultas(clave_animal):
        cursor = conexion.cursor()
        # Consulta para mostrar las consultas de un animal
        consulta = "SELECT * FROM Consultas WHERE clave_animal = %s"
        cursor.execute(consulta, (clave_animal,))
        resultado = cursor.fetchall()
        return resultado
    
    @staticmethod
    def actualizar_consulta(numero_consultas, clave_animal):
        cursor = conexion.cursor()
        # Consulta para actualizar una consulta en la tabla Consultas
        consulta = "UPDATE Consultas SET numero_consultas = %s WHERE clave_animal = %s"
        cursor.execute(consulta, (numero_consultas, clave_animal))
        conexion.commit()
        return True, "Consulta actualizada correctamente."

class Vacunas:
    def __init__(self, numero_vacunas, clave_animal):
        self.numero_vacunas = numero_vacunas
        self.clave_animal = clave_animal
    
    def registrar_vacuna(self):
        cursor = conexion.cursor()
        # Consulta para insertar una vacuna en la tabla Vacunas
        consulta = "INSERT INTO Vacunas (numero_vacunas, clave_animal) VALUES (%s, %s)"
        cursor.execute(consulta, (self.numero_vacunas, self.clave_animal))
        conexion.commit()
        return True, "Vacuna registrada correctamente."
    
    @staticmethod
    def mostrar_vacunas(clave_animal):
        cursor = conexion.cursor()
        # Consulta para mostrar las vacunas de un animal
        consulta = "SELECT * FROM Vacunas WHERE clave_animal = %s"
        cursor.execute(consulta, (clave_animal,))
        resultado = cursor.fetchall()
        return resultado
    
    @staticmethod
    def actualizar_vacuna(numero_vacunas, clave_animal):
        cursor = conexion.cursor()
        # Consulta para actualizar una vacuna en la tabla Vacunas
        consulta = "UPDATE Vacunas SET numero_vacunas = %s WHERE clave_animal = %s"
        cursor.execute(consulta, (numero_vacunas, clave_animal))
        conexion.commit()
        return True, "Vacuna actualizada correctamente."
    
class Servicios:
    def __init__(self, clave_servicio, descripcion_servicio, costo_servicio):
        self.clave_servicio = clave_servicio
        self.descripcion_servicio = descripcion_servicio
        self.costo_servicio = costo_servicio
    
    def registrar_servicio(self):
        cursor = conexion.cursor()
        # Consulta para insertar un servicio en la tabla Servicios
        consulta = "INSERT INTO Servicios (clave_servicio, descripcion_servicio, costo_servicio) VALUES (%s, %s, %s)"
        cursor.execute(consulta, (self.clave_servicio, self.descripcion_servicio, self.costo_servicio))
        conexion.commit()
        return True, "Servicio registrado correctamente."
    
    @staticmethod
    def mostrar_servicios():
        cursor = conexion.cursor()
        # Consulta para mostrar los servicios
        consulta = "SELECT * FROM Servicios"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado
    
    @staticmethod
    def actualizar_servicio(clave_servicio, descripcion_servicio, costo_servicio):
        cursor = conexion.cursor()
        # Consulta para actualizar un servicio en la tabla Servicios
        consulta = "UPDATE Servicios SET descripcion_servicio = %s, costo_servicio = %s WHERE clave_servicio = %s"
        cursor.execute(consulta, (descripcion_servicio, costo_servicio, clave_servicio))
        conexion.commit()
        return True, "Servicio actualizado correctamente."

class Veterinaria:
    def __init__(self, nombre_veterinaria, direccion_veterinaria, telefono_veterinaria):
        self.nombre_veterinaria = nombre_veterinaria
        self.direccion_veterinaria = direccion_veterinaria
        self.telefono_veterinaria = telefono_veterinaria
    
    def registrar_veterinaria(self):
        cursor = conexion.cursor()
        # Consulta para insertar una veterinaria en la tabla Veterinarias
        consulta = "INSERT INTO Veterinarias (nombre_veterinaria, direccion_veterinaria, telefono_veterinaria) VALUES (%s, %s, %s)"
        cursor.execute(consulta, (self.nombre_veterinaria, self.direccion_veterinaria, self.telefono_veterinaria))
        conexion.commit()
        return True, "Veterinaria registrada correctamente."
    
    @staticmethod
    def mostrar_veterinarias():
        cursor = conexion.cursor()
        # Consulta para mostrar las veterinarias
        consulta = "SELECT * FROM Veterinarias"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado
    
    @staticmethod
    def actualizar_veterinaria(nombre_veterinaria, direccion_veterinaria, telefono_veterinaria):
        cursor = conexion.cursor()
        # Consulta para actualizar una veterinaria en la tabla Veterinarias
        consulta = "UPDATE Veterinarias SET direccion_veterinaria = %s, telefono_veterinaria = %s WHERE nombre_veterinaria = %s"
        cursor.execute(consulta, (direccion_veterinaria, telefono_veterinaria, nombre_veterinaria))
        conexion.commit()
        return True, "Veterinaria actualizada correctamente."

class Citas:
    def __init__(self, id_cita, fecha_cita, clave_cliente, clave_empleado, clave_veterinaria, clave_animal, clave_servicio):
        self.id_cita = id_cita
        self.fecha_cita = fecha_cita
        self.clave_cliente = clave_cliente
        self.clave_empleado = clave_empleado
        self.clave_veterinaria = clave_veterinaria
        self.clave_animal = clave_animal
        self.clave_servicio = clave_servicio

    def registrar_cita(self):
        cursor = conexion.cursor()
        # Consulta para insertar una cita en la tabla Citas
        consulta = "INSERT INTO Citas (id_cita, fecha_cita, clave_cliente, clave_empleado, clave_veterinaria, clave_animal, clave_servicio) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(consulta, (self.id_cita, self.fecha_cita, self.clave_cliente, self.clave_empleado, self.clave_veterinaria, self.clave_animal, self.clave_servicio))
        conexion.commit()
        return True, "Cita registrada correctamente."
    
    @staticmethod
    def mostrar_citas():
        cursor = conexion.cursor()
        # Consulta para mostrar las citas
        consulta = "SELECT * FROM Citas"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado
    
    @staticmethod
    def actualizar_cita(id_cita, fecha_cita, clave_cliente, clave_empleado, clave_veterinaria, clave_animal, clave_servicio):
        cursor = conexion.cursor()
        # Consulta para actualizar una cita en la tabla Citas
        consulta = "UPDATE Citas SET fecha_cita = %s, clave_cliente = %s, clave_empleado = %s, clave_veterinaria = %s, clave_animal = %s, clave_servicio = %s WHERE id_cita = %s"
        cursor.execute(consulta, (fecha_cita, clave_cliente, clave_empleado, clave_veterinaria, clave_animal, clave_servicio, id_cita))
        conexion.commit()
        return True, "Cita actualizada correctamente."
    
    