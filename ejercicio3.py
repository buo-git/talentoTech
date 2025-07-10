print("Bienvenido al Aplicativo de registro de compras")
product = input("Ingrese nombre del producto: ")
category = input("Ingrese categoría del producto: ")
buy_price = float(input("Ingrese el precio de compra: "))
iva = float(input("Ingrese el IVA del producto: "))

sell_price = buy_price + (buy_price * iva/100)

print("\nDatos de la compra")
print("\nNombre del producto: ", product, "\nCategoría del producto: ", category, "\nPrecio de compra: ", buy_price, "\nIva aplicado: ", iva, "%")
print("\n------------------")
print("Precio de venta del producto: ", sell_price)

