
def nuevoTema(tema):
    print("\n=====",tema,"=====\n")

print("-----Operadores aritmeticos-----")
print("")
print("Operador division entera(10//3): ", 10//3)
print("Operador potencia (5**3): ", 5**3)

print("")

print("Operadores logicos")
print("====AND====")
print("Operador and (True and False): ", True and False) #False
print("Operador and (True and True): ", True and True) #False
print("Operador and (False and False): ", False and False) #False

print("")

print("==========OR========")
print("Operador or (True and False): ", True or False) #True
print("Operador or (True and True): ", True or True) #True
print("Operador or (False and False): ", False or False) #False

print("")

print("======NOT=========")
print("Operador not (True and False): ", not False) #True
print("Operador not (True and True): ", not True) #False

print("")

print("===Operadores de compreacion===")

print("2==3", 2==3) #False 
print("2<3", 2<3) #True
print("2>3", 2>3)#False 
print("2<=3",2<=3) #True
print("2>=3",2<=3) #True
print("2!=3", 2!=3) #true


nuevoTema("Variables")
variable1=10
_variable=6.2456



nuevoTema("Enteros")
w=105
x=98892598
y = -256
z = 0b00110011
h = 0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

nuevoTema("Flotantes")
x=127
print(x, type(x))
y=0.563739
print(y, type(y))

nuevoTema("Numeros complejos")
x=-46j
y=12+45j
z=2j

print(x, type(x))
print(y, type(y))
print(z, type(z))

nuevoTema("Boolenaos")
lis = [0]
print(lis, "es", bool(lis))
t=()
print(t,"es", bool(t))
new = "hello"
print(new, "es", bool(new))
num = 99
print(num, "es", bool(num))
comp = 1+ 0j
print(comp, "es", bool(comp))
val=None
print(val,"es",bool(val))

nuevoTema("Listas")
a=[10,2-0.5,"Python list"]
print(a)
print(a[1])
a[0]="Hola"
print(a)

nuevoTema("Tuplas")
t=(25,"Tuplas",1+10j,3.1416)
print(t)
print(t[2])
print("t[1:4]")
