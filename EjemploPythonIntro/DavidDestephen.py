def getInteger(texto):
    control = True
    c = 0
    while control or c < 10:
        try:
            return int(input(f"ingrese la {texto} nota: "))
        except:
            print("Ingrese un numero")
        c = c + 1
        if c == 10:
            return 0
def esAprovado(clase, nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    if promedio >= 65:
        print(f"{name} aprobó {clase}")
    else:
        print(f"{name} reprobó {clase}")

name = input("ingrese su nombre: ")

for i in range(1, 5):
    clase = input("ingrese la clase: ")

    try:
        nota1 = getInteger("primer")
        nota2 = getInteger("segunda")
        nota3 = getInteger("tercera")
    except:
        print("Ingrese un numero")
    else:
        esAprovado(clase, nota1, nota2, nota3)