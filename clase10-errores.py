
#Errores
'''
try:
    print("1")
    x=1/0
    print("2")
except:
    print("Salio mal")
print("3")


try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")
print("THE END.")



try:
    y=1/0
except ZeroDivisionError:
        print("Zero problem")
except ArithmeticError:
    print("Aritmetic problem")
print("The end")



def badFun(n):
    try:
        return n / 0
    except:
        print("Error en cualquier parte")
        raise 
try:
    badFun(0)
except ArithmeticError:
    print("Error lanzado por raise")
print("THE END.")


numero = 10
maximo=5
if numero > maximo:
    raise Exception('El número a ingresar no debe ser mayor que {} . el valor ingresado fue: {}'.format(maximo,numero))
    


dict = { 'a' : 'b', 'b' : 'c', 'c' : 'd' }
ch = 'a'
try:
    while True:
        ch = dict[ch]
        print(ch)
except KeyError:
    print('No existe tal clave:', ch)
    
    
    
    
    
try:
    print("1")
    x=1/0
    print("2")
except:
    print ("Hay un !Error¡¡¡ ")
print ("3")





string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('¡Esto no es gracioso!')
    
    
    
    
    
from time import sleep
seconds = 0
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("¡No hagas eso!")
        
        
        
        
lista = [1, 2, 3, 4, 5]
ix = 0
doit = True

while doit:
    try:
        print(lista[ix])
        ix += 1
    except IndexError:
        doit = False

print('Listo')




def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        n = None
    else:
        print("Todo salió bien")
    finally:
        print("Es el momento de decir adiós")
        return n

print(reciproco(2))
print(reciproco(0))




from math import exp
ex = 1
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('El número es demasiado grande.')
    
    


try:
    import math
    import time
    import abracadabra

except:
    print('Una de sus importaciones ha fallado.')
    
    
    '''
