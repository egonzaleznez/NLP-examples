def main(): 
    while True:
        print("1. imprime impares")
        print("2. imprime pares")
        print("3. imprime una consecución")
        print("4. función vacía")
        print("5. fin")
        print("\n")
        opcion = str(input("selecciona una opción: "))
        print("\n")
        
        match opcion:
            case "1":
                impares()
            case "2":
                impares(1)
            case "3":
                consecucion()
            case "4":
                fun_vacia()
                print("listo fun vacía")
                print("\n")
            case "5":
                break
            case _:
                print("invalido")
                print("\n")
    else:
        print("fin de programa")

def fun_vacia():
    pass

def consecucion():
    i = 0

    max_num = input("dame max: ")
    dif_num = input("dame salto: ")
    
    if not max_num:
        numero = 10
    else:
        numero = int(max_num)

    if not dif_num:
        salto = 2
    else:
        salto = int(dif_num)

    for i in range(0,numero,salto):
        print(i)
    else:
        print("fin de la serie")
        print("\n")

#    while i < numero:
#        i = i + salto
#        print(i)
#    else:
#        print("fin de la serie")
#        print("\n")


def impares(flag=0):
    max_num = input("dame max: ")
    if not max_num:
        serie(flag=flag)
    else:
        serie(int(max_num), flag)


def serie(numero=10,flag=0):
    i = 0
    
    while i < numero:
        i = i + 1
    
        if flag == 0:
            if i%2 == 0:
                continue        
            print(i)
        else:
            if i%2 != 0:
                continue        
            print(i)
    else:
        print("fin de la serie")
        print("\n")

main()