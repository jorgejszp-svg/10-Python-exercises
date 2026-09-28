edad = int(input("Dame tu edad: "))
tiene_autorizacion = input("¿Tienes autorización? (si/no): ").lower() == "si"
tiene_identificacion = input("¿Dispones de identificación? (si/no): ").lower() == "si"

es_mayor_de_edad = edad >= 18
acceso_completo = es_mayor_de_edad and tiene_autorizacion and tiene_identificacion
acceso_supervisado = tiene_autorizacion or es_mayor_de_edad
acceso_bloqueado = not tiene_identificacion

print(f"\nEs mayor de edad: {es_mayor_de_edad}")
print(f"Acceso completo: {acceso_completo}")
print(f"Acceso supervisado: {acceso_supervisado}")
print(f"Acceso bloqueado: {acceso_bloqueado}")