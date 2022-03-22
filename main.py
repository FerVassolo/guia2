from ej2 import Bank, BankAccount
from g2ej1 import Lines, Triangle, Point2D

print("#1")
a = Lines([1, 1], [0, 1])
b = Lines([2, 2], [1, 1])
c = Lines([3, 3], [5, 2])

for recta in Lines.rectas:
    print(recta.lenght())


triangulo = Triangle()
print(triangulo.perimeter())
print(triangulo.area())
print(triangulo.isEquilateral())
print(triangulo.isScalane())
print(triangulo.isIsoceles())
print("\n")

print("#2")
c1 = BankAccount(123)
c1.deposit(5000)

c2 = BankAccount(234)
c2.deposit(2000)

macro = Bank(1, "Macro")
macro.agregarCuenta(c1)
macro.agregarCuenta(c2)
macro.transferirDinero(c1, c2, 500)
print(macro.ordenarCuentasCbu())
print(macro.ordenarCuentasBalance())
print("\n")
