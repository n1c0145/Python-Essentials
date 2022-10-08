

def readint(prompt, min, max):
    while True:
        try:   
            v=int(input(prompt))
        
            if v>=-10 and v<=10:
               
                print("The number is:", v)
                break
            else:
                print("Error: el valor no está en el rango permitido")
        except ValueError:
            print("Error en el ingreso")
            
v = readint("Enter a number from -10 to 10: ", -10, 10)


  



def validarNumero(prompt, min, max):
    while (True):
        try:
            print("Ingrese un valor entre ",min," y ",max)
            x = int(input(prompt))
            assert x >= min and x <= max
            return x
        
        except ValueError:
            print("Ingresar solo numeros")
        except:
            print("Error, el valor debe estar dentro del RANGO ")
    
v = validarNumero("Ingrese un valor en el rango:", -100, 100)

print("El número es:", v)