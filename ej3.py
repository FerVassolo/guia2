"""Implemente la clase PhoneBill, que permite registrar movimientos de una cuenta de
teléfonos (duración de la llamada). A medida que se realizan consumos, estos se van
registrando y permiten luego imprimir por pantalla los movimientos, permite además consultar
el saldo de la cuenta. Además, existe la posibilidad de ajustar el precio del segundo en cualquier momento.
"""


class PhoneBill:

    precio = 1 # por segundo

    def __init__(self, saldo):
        self.saldo = saldo

    def movimientos(self, duracion):
        if self.saldo > self.precio * duracion:
            self.saldo -= self.precio * duracion
            return self.saldo
        return "Saldo Insuficiente"

    def saldoActual(self):
        return self.saldo

    @classmethod
    def ajustarPrecio(cls, nuevoPrecio):
        cls.precio = nuevoPrecio

cuenta1 = PhoneBill(50)
PhoneBill.ajustarPrecio(2)
cuenta1.movimientos(15)
print(cuenta1.saldoActual())
