"""
Ejercicio

Crea una clase llamada Punto con sus dos coordenadas X e Y.
Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa 
sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
(Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla.
 La fórmula es la siguiente

"""
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Punto:({},{})".format(self.x, self.y)
    def __str2__(self):
        return("Punto ({self.x}, {self.y})".format(self=self))    
    def cuadrante(self):
        if self.x > 0:
            if self.y > 0:
               return "El punto pertenece al primer cuandrante"
            elif self.y == 0:
               return "El punto se encuentra sobre el eje x"
            else:
               return "El punto pertence al cuarto cuadrante"
        elif self.x == 0:
            if self.y == 0:
                return "El punto es igual al origen"
            else:    
                return "El punto se encuentra sobre el eje y"       
        else:    
            if self.y > 0:
                return "El punto pertenece al segundo cuadrante"
            elif self.y == 0:
                return "El punto se encurntra sobre el eje x"
            else:
                return "El punto pertenece al tercer cuadrante"         
    def Vector(self, other):
        Componente_x = other.x - self.x
        Componente_y = other.y - self.y
        return ("Vector: ({},{})".format(Componente_x, Componente_y))
    def distancia(self,other):
        Componente_x = abs(other.x - self.x)
        Componente_y = abs(other.y - self.y)
        distancia = math.sqrt((Componente_x)^2 + (Componente_y)^2)
        return "Distancia: {}".format(distancia)
