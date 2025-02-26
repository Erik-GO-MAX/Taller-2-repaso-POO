from Producto import Producto

def calcular_promedio_granos(lista_productos):
    acumulado = 0
    for producto in lista_productos:
        if(producto.categoria == "granos"):
            acumulado += producto.precio_total
    return acumulado 

def calcular_promedio_lacteos(lista_productos):
    acumulado = 0
    for producto in lista_productos:
        if(producto.categoria == "lacteos" and producto.precio_neto > 13000):
            acumulado += producto.precio_neto
            #acumulado = acumulado + producto.precio_neto
    return acumulado

def calcular_promedio_verduras(lista_productos):
    acumulado = 0
    promedio = 0
    contador = 0 
    for producto in lista_productos:
        if(producto.categoria == "verduras"):
            acumulado += producto.precio_neto
            contador += 1 
    if(contador > 0):
        promedio = acumulado/contador
    else:
        print("El cliente no adquirio productos de la categoria verduras")
    return promedio

def Calcular_promedio_aseo(lista_productos):
    acumulado =  0
    contador = 0
    for producto in lista_productos:
        if (producto.categoria.lower()=='aseo' and  producto.precio_total < 20000 ):
                acumulado += producto.precio_total
                contador += 1
    if contador == 0:
        return 0
    return acumulado / contador
    

class Main():
    def main():
        for i in range(12):
            nombre = input(f"ingrese el nombre del producto {i + 1}")
            categoria = input(f"ingrese la categoria del producto {i + 1}")
            precio_total = int(input(f"ingrese el precio total del producto {i + 1}"))
            iva = float(input(f"ingrese el iva del producto {i + 1}"))
            mi_producto = Producto(nombre, categoria, precio_total, iva )
            lista_productos.append(mi_producto)
        print(f"El cumulado del precio total de los productos con categoria granos es: {calcular_acumulado_granos(lista_productos)}")
    main()




