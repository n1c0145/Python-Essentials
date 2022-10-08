


file = open('devices.txt','a')
while True:
    newItem=  input("Ingrese el nuevo dispositivo: ")
   
    if newItem == "exit":
        print('Todo listo')
        break
    file.write(newItem + "\n")
file.close()
