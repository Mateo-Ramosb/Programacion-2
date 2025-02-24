from Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, fecha_de_fabricacion, vin_chasis, vin_motor, marca, modelo, precio):
        super().__init__(fecha_de_fabricacion, vin_chasis, vin_motor)
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def obtener_marca(self):
        return self.marca

    def obtener_modelo(self):
        return self.modelo

    def obtener_precio(self):
        return self.precio

    def mostrar_los_datos(self):
        print("Los Detalles del Automovil:")
        print(f"Fecha de Fabricacion: {self.obtener_fecha_de_fabricacion()}")
        print(f"VIN del chasis: {self.obtener_vin_chasis()}")
        print(f"VIN del motor: {self.obtener_vin_motor()}")
        print(f"Marca: {self.obtener_marca()}")
        print(f"Modelo: {self.obtener_modelo()}")
        print(f"Precio: $USD {self.obtener_precio()}")

