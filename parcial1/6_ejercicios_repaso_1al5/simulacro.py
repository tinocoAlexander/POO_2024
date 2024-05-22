"""""
    Crear un programa que calcule y obtenga el total a pagar por un producto determinado
    Se deberá solicitar el nombre o descripcion del producto, cantidad, precio unitario, el total a pagar, el iva 16%
    y el descuento
    Si se compran de 1 a 5 productos se otorga el 10% de descuento, si de 6 a 10 el 15% de descuento
    y si se compran mas de 10 productos el 20% de descuento
"""""
print("Bienvenido a nuestro programa para calcular el total de su compra")
nombre = input("Ingrese el nombre del producto: ")
try:
    cantidad = int(input("Ingrese la cantidad de productos: "))
    precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    precio_total = precio_unitario * cantidad
    if cantidad>=1 and cantidad<=5:
        descuento = 0.10
    elif cantidad>=6 and cantidad<=10:
        descuento = 0.15
    elif cantidad > 10:
        descuento = 0.20
    else:
        descuento = 0.0
    monto_descuento = precio_total * descuento
    precio_con_descuento = precio_total - monto_descuento
    iva = precio_con_descuento * 0.16
    total_a_pagar = precio_con_descuento + iva

    # Mostrar los resultados
    print(f"\nNombre del producto: {nombre}")
    print(f"Cantidad de productos: {cantidad}")
    print(f"Precio unitario: ${precio_unitario:.2f}")
    print(f"Descuento aplicado: ${monto_descuento:.2f}")
    print(f"IVA (16%): ${iva:.2f}")
    print(f"Total a pagar: ${total_a_pagar:.2f}")

except ValueError:
    print("Error, tiene que ser un numero")    