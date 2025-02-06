def main(): 
    while True:
        print("1. imprime texto completo")
        print("2. imprime la primera mitad del texto")
        print("3. imprime la segunda mitad del texto")
        print("4. imprime una sección específica")
        print("5. fin")
        print("\n")
        opcion = str(input("selecciona una opción: "))
        print("\n")
        
        texto = str(input("dame texto: "))
        print(texto)
        tamano = len(texto)
        print("tamaño del texto: ", tamano)
        mitad = round(tamano/2)
        print("mitad texto: ", mitad)
        print("\n")
        
        if opcion == "1":
            print(texto)
            print("\n")
        elif opcion == "2":
            print(texto[:mitad])
            print("\n")
        elif opcion == "3":
            print(texto[mitad:])
            print("\n")
        elif opcion == "4":
            cifra1 = int(input("dame un número: "))
            cifra2 = int(input("dame otro número: "))
            if cifra1 < cifra2 and cifra2 < tamano:
                print(texto[cifra1:cifra2])
                print("\n")
            else:
                print("númeos no validos para imprimir segmento")
                print("\n")
        elif opcion == "5":
            print("fin de programa")
            break
        else:
            print("invalido")
            print("\n")
            
        print("quinta letra: ", texto[4])
        print(texto[-3])
        print("\n")
            
main()

