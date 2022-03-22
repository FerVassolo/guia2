from bankAcount import BankAccount

class Bank:

    def __init__(self, ID, nombre):
        self.ID = ID
        self.nombre = nombre
        self.__cuentas = []

    def agregarCuenta(self, cuenta):
        self.__cuentas.append(cuenta)

    #def quitarCuenta(self, cbu):
        #for indice, obj in enumerate(self.__cuentas): # Use enumerate() to get a counter in a loop
            #if obj.getCBU() == cbu:
                #del self.__cuentas[indice]
    def quitarCuenta(self, cbu):
        aux = [cuenta for cuenta in self.__cuentas if cuenta.getCBU() != cbu]
        self.__cuentas = aux

    def buscarCuenta(self, cbu):
        for indice, obj in enumerate(self.__cuentas):
            if obj.getCBU() == cbu:
                return self.__cuentas[indice]

    def transferirDinero(self, cuentaDa, cuentaRecibe, monto):
        #cuentaDa = balance - monto y cuentaRecibe = balance + monto
        if monto < cuentaDa.getBalance():
            cuentaDa.withraw(monto)
            cuentaRecibe.deposit(monto)
        else:
            return "Saldo Insuficiente"

    def ordenarCuentasCbu(self):
        lista_ordenada = sorted(self.__cuentas, key = lambda cuenta: cuenta.getCBU(), reverse = False)
        ordenada = [i.getCBU() for i in lista_ordenada]
        return ordenada

    def ordenarCuentasBalance(self):
        lista_ordenada = sorted(self.__cuentas, key = lambda cuenta: cuenta.getBalance(), reverse = False)
        ordenada = [i.getBalance() for i in lista_ordenada]
        return ordenada







