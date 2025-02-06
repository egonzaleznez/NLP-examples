def dameDatos():
    mi_string = "1234567"
    mi_lista = [1,2,3,4,5,6,7]
    mi_tupla = (1,2,3,4,5,6,7)
    
    return mi_string, mi_lista, mi_tupla

def imprimeDatos(mi_string = "", mi_lista = [], mi_tupla = ()):
    print("imprimo los datos")
    print(mi_string)
    print(mi_lista)
    print(mi_tupla)
    print("\n")
    
def imprimeElemento(i=0):
    print("imprimo el elemento número: ", i)
    print(mi_string[i])
    print(mi_lista[i])
    print(mi_tupla[i])
    print("\n")
    
def imprimeSección(i=0, j=0, mi_string = "", mi_lista = [], mi_tupla = ()):
    if i <= j and j <= len(mi_lista):
        print("sección de datos escogidos")
        imprimeDatos(mi_string[i:j], mi_lista[i:j], mi_tupla[i:j])
    else:
        print("longitud no valida")
        print("\n")
        
def imprimeSección2(i=0, j=0, mi_string = "", mi_lista = [], mi_tupla = ()):
    if abs(i) <= len(mi_lista) and i <= j and j <= -1:
        print("sección de datos escogidos")
        imprimeDatos(mi_string[i:j], mi_lista[i:j], mi_tupla[i:j])
    else:
        print("longitud no valida")
        print("\n")     
        
def cambiaElemento(i=0, element=0, mi_string = "", mi_lista = [], mi_tupla = ()):
    print("cambio el elemento número: ", i)
    try:
        mi_string[i] = str(element)
    except:
        print("esa operación con strings no se puede")
    else:
        print("modificación exitosa del string")
        
    try:
        mi_lista[i] = element
    except:
        print("esa operación con listas no se puede")
    else:
        print("modificación exitosa de la lista")
        
    try:
        mi_tupla[i] = element
    except:
        print("esa operación con tuplas no se puede")
    else:
        print("modificación exitosa de la tupla")
    finally:
        print("terminé de realizar modificaciones")
        print("\n")
        
    return mi_string, mi_lista, mi_tupla

def agregaElemento(i=0, mi_string = "", mi_lista = [], mi_tupla = ()):
    print("agrega el elemento: ", i)
    mi_string = mi_string + str(i)
    mi_lista = mi_lista + [i]
    mi_lista.append(9)
    mi_tupla = mi_tupla + (i,) # truco, añado otra tupla
    
    return mi_string, mi_lista, mi_tupla

def quitaElemento(i=0, mi_string = "", mi_lista = [], mi_tupla = ()):
    print("quito el elemento: ", i)
    
    try:
        mi_string = mi_string - mi_string[i]
    except:
        print("esa operación con strings no se puede")
    else:
        print("modificación exitosa del string")
    
    try:
         mi_lista = mi_lista - mi_lista[i]
    except:
        print("esa operación con listas no se puede")
    else:
        print("modificación exitosa de la lista")
        
    try:
         mi_tupla = mi_tupla - mi_tupla[i]
    except:
        print("esa operación con tuplas no se puede")
    else:
        print("modificación exitosa de la tupla")
    finally:
        print("terminé de realizar modificaciones")
        print("\n")
    
    return mi_string, mi_lista, mi_tupla

def quitaElemento2(i=0, mi_string = "", mi_lista = [], mi_tupla = ()):
    print("quito el elemento: ", i)
    
    try:
        mi_string = mi_string.replace(str(i), "")
    except:
        print("esa operación con strings no se puede")
    else:
        print("modificación exitosa del string")
    
    try:
         mi_lista.remove(mi_lista[i]) # quita la que está guardano en la posición i
         mi_lista.remove(i) # quita el elemento con valor igual a i
    except:
        print("esa operación con listas no se puede")
    else:
        print("modificación exitosa de la lista")
        
    try:
         temp = list(mi_tupla)
         temp.pop(i) # quita la que está guardado en la posición i
         mi_tupla = tuple(temp)
    except:
        print("esa operación con tuplas no se puede")
    else:
        print("modificación exitosa de la tupla")
    finally:
        print("terminé de realizar modificaciones")
        print("\n")
    
    return mi_string, mi_lista, mi_tupla

def sumaOtro(mi_string1 = "", mi_string2 = "", mi_lista1 = [], mi_lista2 = [], mi_tupla1 = (), mi_tupla2 = ()):
    print("sumo otro")
    mi_string = mi_string1 + mi_string2
    mi_lista = mi_lista1 + mi_lista2
    mi_tupla = mi_tupla1 + mi_tupla2
    
    
    return mi_string, mi_lista, mi_tupla

def insertaElemento(i=0, j=0, mi_lista = []):
    mi_lista.insert(j, i)
    
    return mi_lista

def masCosas():
    mi_lista = [1,2,3,"Hola", True, "Adios", False]
    mi_tupla = (4,5,6,"Hi", False, "Bye", mi_lista, True)
    
    for i in mi_lista:
        print(i)
    print("\n")
    
    for i in mi_tupla:
        print(i)
    print("\n")
    
    for i in range(len(mi_lista)):
        print(mi_lista[i])
    print("\n")
    
    for i in range(len(mi_tupla)):
        print(mi_tupla[i])
    print("\n")

mi_string, mi_lista, mi_tupla = dameDatos()

imprimeDatos(mi_string, mi_lista, mi_tupla)

imprimeElemento(1)

cambiaElemento(1,8, mi_string, mi_lista, mi_tupla)

imprimeDatos(mi_string, mi_lista, mi_tupla)

imprimeSección(0, 2, mi_string, mi_lista, mi_tupla)

imprimeSección2(-7, -2, mi_string, mi_lista, mi_tupla)

mi_string, mi_lista, mi_tupla = agregaElemento(2, mi_string, mi_lista, mi_tupla)

imprimeDatos(mi_string, mi_lista, mi_tupla)

mi_string, mi_lista, mi_tupla = quitaElemento(2, mi_string, mi_lista, mi_tupla)

imprimeDatos(mi_string, mi_lista, mi_tupla)
    
mi_string, mi_lista, mi_tupla = quitaElemento2(2, mi_string, mi_lista, mi_tupla)

imprimeDatos(mi_string, mi_lista, mi_tupla)

mi_string2, mi_lista2, mi_tupla2 = dameDatos()

mi_string, mi_lista, mi_tupla = sumaOtro(mi_string, mi_string2, mi_lista, mi_lista2, mi_tupla, mi_tupla2)

imprimeDatos(mi_string, mi_lista, mi_tupla)

mi_lista = insertaElemento(91, 3, mi_lista)

imprimeDatos(mi_string, mi_lista, mi_tupla)

masCosas()
    
