def areacirculo(r):
    return 3.1416 * r ** 2

print("Calculo del area de un Circulo")
r = int(input("ingrese el diametro: " ) )
areaC =areacirculo(r)
print("Area del Circulo: " + str(areaC) + "\n")