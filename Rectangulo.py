"""
Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
Añade al rectángulo un método llamado base que muestre la base.
Añade al rectángulo un método llamado altura que muestre la altura.
Añade al rectángulo un método llamado area que muestre el area
"""
from Punto import Punto
class Rectangulo(Punto):
    def __init__(self, x1, y1, x2, y2):
        A = super(Punto).__init__(x1,y1)
        B = super(Punto).__init__(x2,y2)
        Diagonal = Punto.Vector(A,B)
        return "Rectangulo cuya diagonal es: {}, y esta formada por los puntos: {} y {}".format(Diagonal, A, B)
