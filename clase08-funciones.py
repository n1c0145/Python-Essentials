
#Funciones

def mensaje():
    print("Type a value")
    
print("Inicio")
mensaje()
print("Fin")



#Funciones con parametros

def saludo(nombre):
    print("Hola",nombre,"\n")
    
saludo("nicolas")
saludo("eduardo")


def suma(a,b):
    print("El resultado de suma es:",a+b)
    
suma(2,5)
    

def address(street,city,postalCode):
    print("Tu direccion es:",street,"Ciudad",city,postalCode)
    
s = input("Street: ")
pC = input("Postal code: ")
c= input("City: ")

address(s,c,pC)


def resta (a,b):
    print(a-b)

resta(a=7,b=6)



def mult(a,b):
    return a*b
    
print(mult(2,4))

resultado=mult(15.8,5.4)
opt=resultado+5
print(opt)

def suma(x,y):
    return x+y
opt2 = suma(opt,10)
print(opt2)



def saludo3(lista):
    for i in lista:
        print("Hola", i)
        
        
saludo3(["Juan","Pedro","Diego"])



def lista2(n):
    lista=[]
    for item in range(n):
        lista.append(item)
        
    return lista

print(lista2(10))


#Funciones lambda

b =lambda x,y: x+y


def suma(*a): #1 * es tupla
    print("\nTipo de datos del argumento:",
         type(a))
    sum = 0
    for n in a:
        sum +=n
        #sum=sum+n

    print("Suma:",sum)

suma(3)
suma(1)
suma(3,5)
suma(4,5,6,7)
suma(1,2,3,5,6)
suma(1,2,3,5,6,7,8,9,10)
suma(1,2,3,5,6,7,8,9,10,11,12,13,14)
suma(1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17)


def keyw(**datos): #2* es diccionario
    print("\nTipo de datos del argumento:",
          type(datos))

    for key, value in datos.items():
        print("{} is {}".format(key,value))

keyw(Firstname="Juan", 
     Lastname="Domínguez", 
     Age=42, 
     Phone=1234567890)
keyw(Firstname="John", 
     Lastname="Wood",
     Email="johnwood@nomail.com",
     Country="Wakanda", 
     Age=25, 
     Phone=9876543210)












