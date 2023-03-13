# Experimentacion
""""
Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
Consulta a que cuadrante pertenecen el punto A, C y D.
Consulta los vectores AB y BA.
(Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
(Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
Crea un rectángulo utilizando los puntos A y B.
Consulta la base, altura y área del rectángulo.
"""
from Punto import Punto
from Rectangulo import Rectangulo
# Creacion de puntos y imprimir por pantalla
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)
print(A.__str__())
print(B.__str__())
print(C.__str__())
print(D.__str__())
# Cuadrante de puntos A,C y D
print(A.cuadrante())
print(C.cuadrante())
print(D.cuadrante())
# Distancia entre A y B, y B y A
print(Punto.distancia(self=A,other=B))
print(Punto.distancia(self=B,other=A))
# Rectangulo con A y B
Rect_Ab = Rectangulo(2, 3, 5, 5)
print(Rect_Ab)
# Altura, base y area
print(Rectangulo.Altura(Rect_Ab))
print(Rectangulo.Base(Rect_Ab))
print(Rectangulo.Area_triang(Rect_Ab))
