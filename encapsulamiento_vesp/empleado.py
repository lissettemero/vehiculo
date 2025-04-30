class Empleado:
    def __init__(self, cedula, nombre, sueldo):
        self._cedula = cedula
        self._nombre = nombre
        self._sueldo = sueldo
        self._eliminado =False


    def __str__(self):
        return f"Empleado: {self.__dict__.__str__()}"

    @property
    def cedula(self):
        return self._cedula

    #@cedula.setter
    #def cedula(self, nueva_cedula):
        #self._cedula = nueva_cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, nuevo_sueldo):
        if nuevo_sueldo > self._sueldo:
            self._sueldo = nuevo_sueldo
    @property
    def eliminado(self):
        return self._eliminado

    @eliminado.setter
    def eliminado(self, nuevo_eliminado):
        self._eliminado = nuevo_eliminado

if __name__ == "__main__":
    empl1 = Empleado(nombre="Juan", sueldo=1000,cedula="0978123465")
    print(empl1)
    empl1.sueldo = 1500
    print(empl1)
    print(empl1.nombre)
    empl1._nombre = "Pedro"
    print(empl1)
    empl1.cedula = "0978123466"
    print(empl1)