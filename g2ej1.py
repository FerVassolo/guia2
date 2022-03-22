from point2d import Point2D
import math
class Lines:

    rectas = []

    def __init__(self, A, B):
        self.A = Point2D(A)
        self.B = B
        self.rectas.append(self)

    def lenght(self):
        return self.A.getDistance(self.B)

class Triangle:

    def __init__(self, a, b, c):
        self.a = Lines.rectas[0].lenght()
        self.b = Lines.rectas[1].lenght()
        self.c = Lines.rectas[2].lenght()

    def isValid(self):
        if self.a < self.b + self.c and self.c < self.b + self.a and self.b < self.a + self.c:
            return True
        else:
            return False

    def perimeter(self):
        # p = perimetro
        if self.isValid() == True:
            return self.a + self.b + self.c
        else:
            return False

    def area(self):
        # a = √s(s-a)(s-b)(s-c)
        # s = p/2
        if self.isValid() == True:
            self.s = self.perimeter()/2
            self.area = math.sqrt(self.s*(self.s - self.a)*(self.s - self.b)*(self.s - self.c))
            return self.area
        else:
            return False

    def isEquilateral(self):
        if self.isValid():
            if self.a == self.b == self.c:
                return "Es equilatero"

        return False

    def isScalane(self):
        if self.isValid():
            if self.a != self.b != self.c:
                return "Es Escaleno"
        return False

    def isIsoceles(self):
        if self.isValid():
            if self.isEquilateral() == False and self.isScalane() == False:
                return "Es Isoceles"
        return False



