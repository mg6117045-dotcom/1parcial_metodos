#ejercicio 1
#x = [2,4,5,7,8]
#y = [60,75,80,90,95]

#ejercicio 2
#x = [1,3,4,6]
#y = [15,25,30,45]

#ejercicio 3
#x = [20,25,30,35,40]
#y = [50,58,65,75,82]

#tarea
#y = [5,3,7,2,8]
#x = [11,6,10,6,12]

#x = [3,4,6,4,2,5]
#y = [6,8,9,5,4.5,9.5]

#x= [5,3,7,2,8]
#y= [11,6,10,6,12]

#x = [2,3,4,5,6,7,8,9,10,11]
#y = [60,65,70,75,80,85,90,95,100,105]
#f0
def media(x):
    return sum(x) / len(x)
#f1
def diferencia_cuadrado(x):
    la_media = media(x)
    la_diferencia = 0
    for i in x:
        la_diferencia = la_diferencia + (i - la_media) * (i - la_media)
    return la_diferencia

#f2
def diferencia_xy(x, y):
    mediax = media(x)
    mediay = media(y)
    lista_xy = [(a - mediax) * (b - mediay) for a, b in zip(x, y)]
    sumatoria = sum(lista_xy)
    return sumatoria
    
    
#es la que se multiplica
def obtener_b1(x,y):
    diferencia = diferencia_xy(x,y)
    diferencia_cuadrados = diferencia_cuadrado(x)
    return diferencia / diferencia_cuadrados

#el valor 
def obtener_b0(x, y):
    mediay = media(y)
    mediax = media(x)
    b1 = obtener_b1(x,y)
    return mediay  - (b1 * mediax)

# mostrar la ecuacion
def obtener_ecuacion(x, y):
    b0 = obtener_b0(x, y)
    b1 = obtener_b1(x, y)
    print(f"La ecuacion es: y = {b0} + ({b1})x")

def obtener_valorpron(x,y,z):
    b0 = obtener_b0(x, y)
    b1 = obtener_b1(x, y)
    m = b0 + b1 * z
    obtener_ecuacion(x, y)
    print(f"el valor pronosticado es: {m}")
    
    



