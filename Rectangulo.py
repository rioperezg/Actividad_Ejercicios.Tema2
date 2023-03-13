"""
Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
Añade al rectángulo un método llamado base que muestre la base.
Añade al rectángulo un método llamado altura que muestre la altura.
Añade al rectángulo un método llamado area que muestre el area
"""
from Punto import Punto

class Rectangulo:
    def __init__(self, x1, y1, x2, y2):
        P = Punto(x1,y1)
        Q = Punto(x2,y2)
        self = Punto.Vector(self=P, other=Q)
        
    def base(self):
        base = abs(self.x1 - self.x2)
        return "Base del rectangulo: ({},0)".format(base)
    
        
# print(Rectangulo.__init__(x1=1,y1=3,x2=6,y2=4))
rect = Rectangulo(1,2,5,3)
print(rect)
# print(rect.base())
