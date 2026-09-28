base = float(input("Dame la base del rectángulo: "))
altura = float(input("Dame la altura del rectángulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = (base**2 + altura**2) ** 0.5

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")
print(f"Diagonal: {diagonal:.2f}")