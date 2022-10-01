
user=input("Ingrese su usuario: ")
password=input("Ingrese su contraseña: ")


if user=="test" and password=="test123":
    print('\n'+'Bienvenido')
    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")
    edad=int(input("Ingrese su edad: "))
    direccion=input("Ingrese su direccion: ")
    
    print("\n"+"Nombre: "+nombre+"\n"+"Apellido: "+apellido+"\n"+
          "Edad: "+str(edad)+"\n"+"Direccion: "+direccion)
    
else:
    
    print('\n'+'Usuario o contraseña incorrectos')
