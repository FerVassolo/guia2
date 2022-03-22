"""En Python los objetos se pueden comparar por igualdad (==) o por identidad (is).
 Si dos objetos son idénticos, también son iguales.
 Sin embargo, dos objetos pueden ser iguales sin ser idénticos.
  Por ejemplo, dos variables pueden tener el mismo valor, pero apuntar a dos objetos diferentes.

Implemente la clase Citizen,
la cual permita identificar ciudadanos a partir de su DNI, nombre y apellido y permita compararlos a partir de su edad.
Defina los métodos mágicos: __eq__,__le__,__lt__,__ge__,__gt__
The correspondence between operator symbols and method names is as follows:
 x<y calls x.__lt__(y), x<=y calls x.__le__(y), x==y calls x.__eq__(y),
  x!=y and x<>y call x.__ne__(y), x>y calls x.__gt__(y),
  and x>=y calls x.__ge__(y). (de documentacion de python)

"""

class Citizen:

    def __init__(self, dni, nombre, apellido, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __eq__(self, other):
        if isinstance(other, Citizen):
            return self.edad == other.edad

    def __le__(self, other):
        if isinstance(other, Citizen):
            return self.edad < other.edad


    def __lt__(self, other):
        return self.edad <= other.edad

    def __ne__(self, other):
        # x!=y and x<>y call x.__ne__(y)
        if isinstance(other, Citizen):
            if self.edad != other.edad:
                return True
        return False



fer = Citizen(44505661, "Fer", "Vassolo", 19)
lio = Citizen(22222222, "Lio", "Messi", 34)


print(fer.__le__(lio))




