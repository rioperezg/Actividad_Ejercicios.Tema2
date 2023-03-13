"""
Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
Añade al rectángulo un método llamado base que muestre la base.
Añade al rectángulo un método llamado altura que muestre la altura.
Añade al rectángulo un método llamado area que muestre el area
"""
from Punto import Punto
from Rectangulo import Base
from Rectangulo import Altura

class Rectangulo:
    def __init__(self, x1, y1, x2, y2):
        P = Punto(x1,y1)
        Q = Punto(x2,y2)
        self.P = P
        self.Q = Q
        self = Punto.Vector(self=P, other=Q)
        
    def Base(self):
        base = abs(self.P.x - self.Q.x)
        print("Base del rectangulo:")
        return base
    def Altura(self):
        altura = abs(self.P.y - self.Q.y)
        print("Altura del rectangulo:")
        return altura
    def Area_triang(self):
        base = self.Base
        altura = self.Altura
        Area = (base*altura)/2
        return "Area del triangulo: {}, u^2".format(Area)        
# print(Rectangulo.__init__(x1=1,y1=3,x2=6,y2=4))
rect = Rectangulo(1,2,5,3)
# print(rect)
print(rect.Base())
print(rect.Altura())
print(rect.Area_triang())