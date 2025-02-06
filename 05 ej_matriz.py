import random as rand
import math


def main():
    while True:      
        print("1. Imprime un numeron aleatorio")
        print("2. Imprime los índices una matriz")
        print("3. deletrea una palabra")
        print("4. calcular una raíz cuadrada")
        print("5. Fin")
        print("\n")
        opcion = str(input("selecciona una opción: "))
        print("\n")
        
        match opcion:
            case "1":
                print("\n")
                numero = num_rand()
                print("num aleatorio: ", numero)
                print("\n")
            case "2":
                print("\n")
                imprime_mat()
            case "3":
                print("\n")
                deletrea()
            case "4":
                print("\n")
                num = int(input("dame un número: "))
                sol = cal_raiz(num)
                print(sol)
            case "5":
                r = float(input("dame el radio: "))
                area = area_circ(r)
                print(area)
            case "6":
                break
            case _:
                print("invalido")

def area_circ(radio):
    val_area = math.pi * (radio **2)
    
    return val_area

def cal_raiz(numero=0):
    respuesta = round(math.sqrt(numero),4)
    
    return respuesta 


def num_rand():
    num = round(rand.random()*100,1)
    
    return num

def imprime_mat():

    num_ren = int(input("dame num de renglones: "))
    num_col = int(input("dame num de columnas: "))
    print("\n")

    for i in range(num_ren):
        for j in range(1, num_col+1):
            celda = "a"+str(i+1)+","+str(j)
            print(celda, end=" ")
        print()
        
def deletrea():
    palabra = input("dame una palabra: ")
    print(palabra)
    
    for letra in palabra:
        print(letra)



main()



