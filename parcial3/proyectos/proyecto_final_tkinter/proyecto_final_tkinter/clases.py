from conexion import *
class Personas:
    def __init__(self, CURP_persona, nombre_persona, apellidop_persona, apellidom_persona, edad_persona, telefono_persona, email_persona, direccion_persona, contrasena_persona, escuela_persona):
        self.CURP_persona = CURP_persona
        self.nombre_persona = nombre_persona
        self.apellidop_persona = apellidop_persona
        self.apellidom_persona = apellidom_persona
        self.edad_persona = edad_persona
        self.telefono_persona = telefono_persona
        self.email_persona = email_persona
        self.direccion_persona = direccion_persona
        self.contrasena_persona = contrasena_persona
        self.escuela_persona = escuela_persona

    def registrar(self):
        try:
            cursor.execute(
                "insert into personas values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.CURP_persona, self.nombre_persona, self.apellidop_persona, self.apellidom_persona, self.edad_persona, self.telefono_persona, self.email_persona, self.direccion_persona, self.contrasena_persona, self.escuela_persona)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def mostrar():
        try:
            cursor.execute(
                "select * from personas"
            )
            return cursor.fetchall()
        except:
            return None
    
class Estudiantes:
    def __init__(self, matricula_estudiante, grado_estudiante, grupo_estudiante, promedio_estudiante, modalidad_estudiante, carrera_estudiante, privilegio, CURP_persona):
        self.matricula_estudiante = matricula_estudiante
        self.grado_estudiante = grado_estudiante
        self.grupo_estudiante = grupo_estudiante
        self.promedio_estudiante = promedio_estudiante
        self.modalidad_estudiante = modalidad_estudiante
        self.carrera_estudiante = carrera_estudiante
        self.privilegio = privilegio
        self.CURP_persona = CURP_persona
    
    def registrar(self):
        try:
            cursor.execute(
                "insert into estudiantes values(%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.matricula_estudiante, self.grado_estudiante, self.grupo_estudiante, self.promedio_estudiante, self.modalidad_estudiante, self.carrera_estudiante, self.privilegio, self.CURP_persona)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def mostrar():
        try:
            cursor.execute(
                "select * from estudiantes"
            )
            return cursor.fetchall()
        except:
            return None
        

    def cambiar_contraseña(self, nueva_contraseña):
        try:
            cursor.execute(
                "update personas set contrasena_persona=%s where CURP_persona=%s",
                (nueva_contraseña, self.CURP_persona)
            )
            conexion.commit()
            return True
        except:
            return False
    
class Profesores:
    def __init__(self, matricula_profesor, puesto_profesor, salario_profesor, antiguedad_profesor, titulo_profesor, privilegio, CURP_persona):
        self.matricula_profesor = matricula_profesor
        self.puesto_profesor = puesto_profesor
        self.salario_profesor = salario_profesor
        self.antiguedad_profesor = antiguedad_profesor
        self.titulo_profesor = titulo_profesor
        self.privilegio = privilegio
        self.CURP_persona = CURP_persona

    def registrar(self):
        try:
            cursor.execute(
                "insert into profesores values(%s,%s,%s,%s,%s,%s,%s)",
                (self.matricula_profesor, self.puesto_profesor, self.salario_profesor, self.antiguedad_profesor, self.titulo_profesor, self.privilegio, self.CURP_persona)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def mostrar():
        try:
            cursor.execute(
                "select * from profesores"
            )
            return cursor.fetchall()
        except:
            return None
    
    def añadir_calificacion(self, matricula_estudiante, calificacion):
        try:
            cursor.execute(
                "insert into calificaciones values(%s,%s,%s)",
                (self.matricula_profesor, matricula_estudiante, calificacion)
            )
            conexion.commit()
            return True
        except:
            return False
        
    def actualizar_calificacion(self, matricula_estudiante, calificacion):
        try:
            cursor.execute(
                "update calificaciones set calificacion=%s where matricula_profesor=%s and matricula_estudiante=%s",
                (calificacion, self.matricula_profesor, matricula_estudiante)
            )
            conexion.commit()
            return True
        except:
            return False

    def eliminar_calificacion(self, matricula_estudiante):
        try:
            cursor.execute(
                "delete from calificaciones where matricula_profesor=%s and matricula_estudiante=%s",
                (self.matricula_profesor, matricula_estudiante)
            )
            conexion.commit()
            return True
        except:
            return False
    
    def consultar_calificaciones(self):
        try:
            cursor.execute(
                "select * from calificaciones where matricula_profesor=%s",
                (self.matricula_profesor,)
            )
            return cursor.fetchall()
        except:
            return None
    
class Materias:
    def __init__(self, clave_materia, nombre_materia, descripcion_materia, creditos_materia, matricula_profesor):
        self.clave_materia = clave_materia
        self.nombre_materia = nombre_materia
        self.descripcion_materia = descripcion_materia
        self.creditos_materia = creditos_materia
        self.matricula_profesor = matricula_profesor

    def registrar(self):
        try:
            cursor.execute(
                "insert into materias values(%s,%s,%s,%s,%s)",
                (self.clave_materia, self.nombre_materia, self.descripcion_materia, self.creditos_materia, self.matricula_profesor)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def mostrar():
        try:
            cursor.execute(
                "select * from materias"
            )
            return cursor.fetchall()
        except:
            return None
    
    @staticmethod
    def actualizar(clave_materia, nombre_materia, descripcion_materia, creditos_materia, matricula_profesor):
        try:
            cursor.execute(
                "update materias set nombre_materia=%s,descripcion_materia=%s,creditos_materia=%s,matricula_profesor=%s where clave_materia=%s",
                (nombre_materia, descripcion_materia, creditos_materia, matricula_profesor, clave_materia)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(clave_materia):
        try:
            cursor.execute(
                "delete from materias where clave_materia=%s",
                (clave_materia,)
            )
            conexion.commit()
            return True
        except:
            return False
    
class Calificaciones:
    def __init__(self, id_calificacion, calificacion, observaciones, clave_materia, matricula_estudiante):
        self.id_calificacion = id_calificacion
        self.calificacion = calificacion
        self.observaciones = observaciones
        self.clave_materia = clave_materia
        self.matricula_estudiante = matricula_estudiante
    
    def registrar(self):
        try:
            cursor.execute(
                "insert into calificaciones values(%s,%s,%s,%s,%s)",
                (self.id_calificacion, self.calificacion, self.observaciones, self.clave_materia, self.matricula_estudiante)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def actualizar(id_calificacion, calificacion, observaciones):
        try:
            cursor.execute(
                "UPDATE calificaciones SET calificacion=%s, observaciones=%s WHERE id_calificacion=%s",
                (calificacion, observaciones, id_calificacion)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar la calificación: {e}")
            return False
        
    @staticmethod
    def eliminar(matricula_estudiante, clave_materia):
        try:
            cursor.execute(
                "DELETE FROM calificaciones WHERE matricula_estudiante=%s AND clave_materia=%s",
                (matricula_estudiante, clave_materia)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar la calificación: {e}")
            return False
    @staticmethod
    def consultar_por_matricula(matricula_estudiante):
        try:
            cursor.execute(
                "SELECT id_calificacion, calificacion, observaciones, clave_materia, matricula_estudiante FROM calificaciones WHERE matricula_estudiante = %s",
                (matricula_estudiante,)
            )
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar las calificaciones: {e}")
            return None
    
    @staticmethod
    def mostrar():
        try:
            cursor.execute(
                "select * from calificaciones"
            )
            return cursor.fetchall()
        except:
            return None