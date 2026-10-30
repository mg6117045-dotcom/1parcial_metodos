s = int(input("Precio: "))
f = int(input("Costo fijo: "))
v = int(input("Venta variable: "))
x = int(input("Unidades: "))

ingresos = s * x
costos = f + v * x

print("Punto de equilibrio:", f / (s - v))
print("Ganancia:", ingresos - costos)
