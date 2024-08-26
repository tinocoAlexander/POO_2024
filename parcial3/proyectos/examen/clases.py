from conexion import *
class Revisiones:
    def __init__(self, no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula):
        self.no_revision = no_revision
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiofrenos = cambiofrenos
        self.otros = otros
        self.matricula = matricula

    def insertar(self):
        try:
            cursor.execute(
                "insert into revisiones values(%s,%s,%s,%s,%s,%s)",
                (self.no_revision, self.cambiofiltro, self.cambioaceite, self.cambiofrenos, self.otros, self.matricula)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from revisiones"
            )
            return cursor.fetchall()
        except:
            return None
        
    @staticmethod
    def actualizar(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros):
        try:
            cursor.execute(
                "UPDATE revisiones SET cambiofiltro=%s, cambioaceite=%s, cambiofrenos=%s, otros=%s WHERE no_revision=%s",
                (cambiofiltro, cambioaceite, cambiofrenos, otros, no_revision)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def eliminar(no_revision):
        try:
            cursor.execute(
                "delete from revisiones where no_revision=%s",
                (no_revision,)
            )
            conexion.commit()
            return True
        except:
            return False

class Autos:
    def __init__(self, matricula, marca, modelo, color, nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif
    
    def insertar(self):
        try:
            cursor.execute(
                "insert into autos values(%s,%s,%s,%s,%s)",
                (self.matricula, self.marca, self.modelo, self.color, self.nif)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from autos"
            )
            return cursor.fetchall()
        except:
            return None
    
    @staticmethod
    def actualizar(matricula, marca, modelo, color):
        try:
            cursor.execute(
                "UPDATE autos SET marca=%s, modelo=%s, color=%s WHERE matricula=%s",
                (marca, modelo, color, matricula)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def eliminar(matricula):
        try:
            cursor.execute(
                "delete from autos where matricula=%s",
                (matricula,)
            )
            conexion.commit()
            return True
        except:
            return False

class Clientes:
    def __init__(self, nif, nombre, direccion, ciudad, tel):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel
    
    def insertar(self):
        try:
            cursor.execute(
                "insert into clientes values(%s,%s,%s,%s,%s)",
                (self.nif, self.nombre, self.direccion, self.ciudad, self.tel)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from clientes"
            )
            return cursor.fetchall()
        except:
            return None
        
    @staticmethod
    def actualizar(nif, nombre, direccion, ciudad, tel):
        try:
            cursor.execute(
                "UPDATE clientes SET nombre=%s, direccion=%s, ciudad=%s, tel=%s WHERE nif=%s",
                (nombre, direccion, ciudad, tel, nif)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(nif):
        try:
            cursor.execute(
                "delete from clientes where nif=%s",
                (nif,)
            )
            conexion.commit()
            return True
        except:
            return False

class Usuarios:
    def __init__(self, email_usuario, contrasena_usuario):
        self.email_usuario = email_usuario
        self.contrasena_usuario = contrasena_usuario
    
    def insertar(self):
        try:
            cursor.execute(
                "insert into usuarios values(%s,%s)",
                (self.email_usuario, self.contrasena_usuario)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from usuarios"
            )
            return cursor.fetchall()
        except:
            return None
