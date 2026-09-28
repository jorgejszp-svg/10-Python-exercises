entradas = int(input("cuantas entradas tienes: "))
grupos = int(input("cuantos grupos la recibiran: "))

entradas_por_grupo = entradas // grupos
sobrantes = entradas % grupos

print(f"Cada grupo recibe: {entradas_por_grupo} entradas")
print(f"Entradas sin repartir: {sobrantes}")