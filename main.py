class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevoColor):
        listaColores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if nuevoColor in listaColores:
            self.color = nuevoColor


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevoRegistro):
        self.registro = nuevoRegistro

    def asignarTipo(self, nuevoTipo):
        if nuevoTipo == "gasolina" or nuevoTipo == "electrico":
            self.tipo = nuevoTipo

class Auto:
    cantidadCreados = ""

    def __init__(self, modelo, precio,asientos:list, marca, motor:Motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos (self):
        contador = 0
        for i in range(len(self.asientos)):
            if isinstance (self.asientos[i], Asiento):
                contador = contador + 1
        return contador

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for asiento in self.asientos:
                if isinstance(asiento, Asiento):
                    if (self.registro != asiento.registro):
                        return "Las piezas no son originales"
            return "Auto original"
        return "Las piezas no son originales"