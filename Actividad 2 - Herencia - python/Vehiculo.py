class Vehiculo:
    def __init__(self, fecha_de_fabricacion, vin_chasis, vin_motor):
        self.fecha_de_fabricacion = fecha_de_fabricacion
        self.vin_chasis = vin_chasis
        self.vin_motor = vin_motor

    def obtener_fecha_de_fabricacion(self):
        return self.fecha_de_fabricacion

    def obtener_vin_chasis(self):
        return self.vin_chasis

    def obtener_vin_motor(self):
        return self.vin_motor


