"""
Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
Añade al rectángulo un método llamado base que muestre la base.
Añade al rectángulo un método llamado altura que muestre la altura.
Añade al rectángulo un método llamado area que muestre el area
"""
from Punto import Punto
import main


class Rectangulo:
    def __init__(self, x1, y1, x2, y2):
        P = Punto(x1,y1)
        Q = Punto(x2,y2)
        self.P = P
        self.Q = Q
        self = Punto.Vector(self=P, other=Q)
        
    def Base(self):
        base = abs(self.P.x - self.Q.x)
        self.base = base
        print("Base del rectangulo:")
        return base
    def Altura(self):
        altura = abs(self.P.y - self.Q.y)
        self.altura = altura
        print("Altura del rectangulo:")
        return altura
    def Area_triang(self):
        base_tr = self.base
        altura_tr = self.altura
        Area = (base_tr*altura_tr)/2
        return "Area del triangulo: {} u^2".format(Area)        
if __name__=="_main_":
    main()
