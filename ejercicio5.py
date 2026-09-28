nombre = input("dame tu nombre: ")
horas = float(input("dame las horas que trabajaste: "))
paga = float(input("dame el precio pagado por hora: "))
porcentaje = float(input("dame el porcentaje de retencion: "))

salarioBruto = horas * paga
importeRetencion = salarioBruto * (porcentaje / 100)
salarioNeto = salarioBruto - importeRetencion

print(f"Trabajador: {nombre}")
print(f"Salario Bruto: {salarioBruto:.2f} €")
print(f"Retención ({porcentaje}%): {importeRetencion:.2f} €")
print(f"Salario Neto: {salarioNeto:.2f} €")