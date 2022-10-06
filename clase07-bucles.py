#For

lista2=[]

lista=["R1","R2","R3","R4","S1","S2"]

        
        
for item in lista:
  if "R" in item:
      print(item)
      
     
for item in lista:
  if "S" in item:
      lista2.append(item)
      print(lista2)
      

     
for i in range(1,10,1):
    print(i)
    
   
#while

numero = input("Ingrese el numero a contar")
numero = int(numero)
contador=1
while contador <= numero:
    print(contador)
    contador+=1    #contador=contador+1
    
    
numero = input("Ingrese el numero a contar")
numero = int(numero)
contador=1
while True:
    print(contador)
    contador+=1    #contador=contador+1
    if contador>numero:
        break
    

    