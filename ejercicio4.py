segundos_totales = int(input("dame los segundos: "))

horas = segundos_totales // 3600
minutos = (segundos_totales % 3600) // 60
segundos = segundos_totales % 60

print(f"Son {horas} horas, {minutos} minutos y {segundos} segundos.")