import math

class Point2D:

    maxDistanceToOrigin = []

    def __init__(self, point):
        self.point = point
        self.maxDistanceToOrigin.append(self)

    def getDistance(self, punto):
        self.punto = punto
        #tengo dos puntos, la distancia de ambos es terorema de pitagoras.
        # C1 es la diferencia en el eje X y C2 en el eje Y
        self.distancia = math.sqrt(math.pow(self.point[0] - self.punto[0], 2) + math.pow(self.point[1] - self.punto[1], 2))
        return self.distancia

    def addPoint(self, punto):
        self.punto = punto
        self.resultado = self.point[0] + self.punto[0], self.point[1] + self.punto[1]
        return self.resultado

    def getX(self):
        return self.point[0]

    def getY(self):
        return self.point[1]

    def getDistanceToOrigin(self):
        self.origen = (0, 0)
        return self.getDistance(self.origen)

p1 = Point2D([1, 2])
p2 = Point2D([1, 2])
print(p1.addPoint(p2.point))
