"""
4 clases
3 notas
APR RPB
"""

class Clases:
    def __init__(self, nombre):
        self.nombre = nombre

class Alumno:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombreCompleto(self):
        print(f"el nombre completo es : "
              f"{self.nombre} {self.apellido}")

clase = Clases("110")

print(f"nombre de la clase {clase.nombre}")

alumno = Alumno("Cons", "Sorto")
alumno.nombreCompleto()