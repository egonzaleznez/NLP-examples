# código de un programa dentro de un loop

# creamos un loop infinito
while True:
    # Mostramos opciones
    print("Mini calculadora")
    print("\n")
    print("Selecciona una de las siguientes opciones:")
    print("1 Suma a + b")
    print("2 Resta a - b")
    print("3 Potencia a^b")
    print("4 Raíz cuadrada de a")
    print("0 Fin del programa")
    print("\n")
    
    # esperamos una opción del usuario
    opcion = input("Opción seleccionada: ")#int(input("Opción seleccionada: "))
    
    # identificamos la opción del usuario
    match opcion:
        case "1":
            a = int(input("Dame a: "))
            b = int(input("Dame b: "))
            print("Suma: ", a+b)
            print("\n")
        case "2":
            a = int(input("Dame a: "))
            b = int(input("Dame b: "))
            print("Resta: ", a-b)
            print("\n")
        case "3":
            a = int(input("Dame a: "))
            b = int(input("Dame b: "))
            print("Potencia: ", a**b)
            print("\n")
        case "4":
            a = int(input("Dame a: "))
            print("Raíz cuadrada: ", a**.5)
            print("\n")
        case "0":
            print("Fin del programa")
            break
        case _:
            print("Opción invalida, selecciona otra opción")
            print("\n")





