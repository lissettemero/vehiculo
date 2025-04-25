def _init_(self, marca: str, modelo: str, color: str = None, anio: int = 2025, tipo=None, motor=None, transmision=None,
           combustible=None, velocidad_maxima=None, precio=None):
    self._marca = marca
    self._modelo = modelo
    self._anio = anio
    self._color = color
    self.tipo = tipo
    self.motor = motor
    self.transmision = transmision
    self.combustible = combustible
    self.velocidad_maxima = velocidad_maxima
    self.precio = precio


def mostrar_info(self):
    print(f"Marca: {self.marca}")
    print(f"Modelo: {self.modelo}")
    print(f"Año: {self.año}")
    print(f"Color: {self.color}")
    print(f"Tipo: {self.tipo}")
    print(f"Motor: {self.motor}")
    print(f"Transmisión: {self.transmision}")
    print(f"Combustible: {self.combustible}")
    print(f"Velocidad Máxima: {self.velocidad_maxima} km/h")
    print(f"Precio: ${self.precio}")


def calcular_impuesto(self, tasa_impuesto):
    impuesto = self.precio * tasa_impuesto / 100
    print(f"El impuesto sobre el vehículo es: ${impuesto}")


'''
classe que representa un objeto de la clase vehiculo
'''


def _str_(self):
    # return f'Vehiculo: [marca={self._marca}, modelo={self._modelo}, color={self._color}]'
    return F'Vehiculo: {self._dict.str_()}'


if _name == "main_":
    v1 = Vehiculo('BMW', 'Arizona', 'color')
    print(v1._marca)
    print(v1._modelo)
    print(v1._color)
    print(v1._anio)
    print(v1)

    v2 = Vehiculo('ford', 'f150', 'negro', 2024)
    print(v2._marca)
    print(v2._modelo)
    print(v2._color)
    print(v2._anio)

    v3 = Vehiculo('ford', 'f150', 'negro', "dos mil veintitres")
    print(v3._marca)
    print(v3._modelo)
    print(v3._color)
    print(v3._anio)

    V4 = Vehiculo('CHEVROLET', 'SAILE')
    print(V4._marca)
    print(V4._modelo)

    v5 = Vehiculo('ford', 'fiesta')
    print(v5)