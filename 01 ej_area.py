# código costo total terreno

# pido variables
a = int(input("dame a: "))
b = int(input("dame b: "))
c = int(input("dame c: "))
d = int(input("dame d: "))

# calcular áreas
a1 = a * b
a2 = (b * d)/2
a3 = (b * c)/2

# calcular área total del terreno
att = a1 - a2 - a3

# calcular valor del terreno 
vtt = att * 3450

print("el valor del terreno es: ", vtt)

