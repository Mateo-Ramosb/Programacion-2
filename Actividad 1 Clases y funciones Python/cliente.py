from datetime import datetime

class Cliente:
    def __init__(self, cedula, nombre, apellido, telefono, correo, direccion, fecha_nacimiento):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
    
    def obtener_datos(self):
        return {
            "Cédula": self.cedula,
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Teléfono": self.telefono,
            "Correo": self.correo,
            "Dirección": self.direccion,
            "Fecha de nacimiento": self.fecha_nacimiento
        }
    
    def calcular_edad(self):
        anio_nacimiento = int(self.fecha_nacimiento[:4])
        anio_actual = datetime.now().year
        return anio_actual - anio_nacimiento