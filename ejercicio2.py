producto = input("producto: ")
cantidad = int(input("cantidad: "))
iva = float(input("iva: "))
precio = float(input("precio: "))

opcion = input("dame una opcion, 1 para el importe sin iva, 2 para el importe del iva y 3 para el precio final: ")

importeSinIva = precio * cantidad
importeIva = importeSinIva * (iva / 100)
importeFinal = importeIva + importeSinIva 

if opcion == "1":
    print("el importe sin iva de tu producto,", producto, "es", importeSinIva)
elif opcion == "2":
    print("el importe del iva de tu producto,", producto, "es", importeIva)
elif opcion == "3":
    print("el precio final de tu producto,", producto, "es", importeFinal)
else:
    print("opcion no valida")