# código que calcula el costo total terreno usand funciones


def main():
    while True:
    
        print("Soy un multiprograma, selecciona opción: ")
        print("\n")
        print("1: Programa área triángulo * n")
        print("2: Programa costo del terreno")
        print("0 Fin del programa")
        print("\n")
        opcion = (input("Dame opción: "))
        
        match opcion:
            case "1":
                res = area_trian_n()
                print ("res: ", res)
                print("\n")
            case "2":
                codigo_costo_terreno()
            case "0":
                print("Fin del programa")
                break
            case _:
                print("Opción invalida, selecciona otra opción")
                print("\n")
                
def area_trian_n():
   # pido variables
    n = int(input("dame n: "))
    a = int(input("dame a: "))
    b = int(input("dame b: "))
    
    return n * area_triangulo(a, b)
    
def codigo_costo_terreno():
    
    # pido variables
    a, b, c, d = pido_variables()
    # calculo las áreas
    a1 = area_rectangulo(a, b)
    a2 = area_triangulo(b, d)
    a3 = area_triangulo(b, c)
    # calculo el costo
    vtt = costo_total(a1, a2, a3)
    
    print("el valor del terreno es: ", vtt)
    
def pido_variables():

    # pido variables
    a = int(input("dame a: "))
    b = int(input("dame b: "))
    c = int(input("dame c: "))
    d = int(input("dame d: "))
    datos = [a, b, c, d]
    
    return datos

def area_rectangulo(base = 1, altura = 1):
    
    # calcular área del rectángulo
    area = base * altura
    
    return area

def area_triangulo(base = 1, altura = 1):
    
    # calcular área del triángulo
    area = (base * altura)/2
                   
    return area
                   
def costo_total(area1, area2, area3):   
    
    # calcular área total del terreno
    att = area1 - area2 - area3
    # calcular valor del terreno 
    vtt = att * 3450
    
    return vtt
                   
main()



