
nombre_cliente = input("Nombre del cliente: ")
nombre_producto = input("Nombre del producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad comprada: "))
porcentaje_descuento = float(input("Porcentaje de descuento: "))
porcentaje_iva = float(input("Porcentaje de IVA: "))

subtotal = precio_unitario * cantidad
importe_descuento = subtotal * (porcentaje_descuento / 100)
precio_con_descuento = subtotal - importe_descuento
importe_iva = precio_con_descuento * (porcentaje_iva / 100)
total_pagar = precio_con_descuento + importe_iva

print("\n" + "=" * 40)
print(f"CLIENTE: {nombre_cliente}")
print("-" * 40)
print(f"Producto:                  {nombre_producto:>15}")
print(f"Cantidad:                  {cantidad:>15}")
print(f"Subtotal:              {subtotal:>10.2f} €")
print(f"Descuento:             {importe_descuento:>10.2f} €")
print(f"IVA:                   {importe_iva:>10.2f} €")
print("-" * 40)
print(f"TOTAL:                 {total_pagar:>10.2f} €")
print("=" * 40)