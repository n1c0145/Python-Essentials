
#Creacion de List
lista=[5,9.0,'test',True,5]
print(len(lista),lista)
print(lista[0])
lista[0]=15
del lista[4]

#Tupla
tupla=(5,6,7,"Hola",5)
print(tupla[-1])

#Diccionario

dict1={"R1":"10.0.0.1",
       "R2":"10.0.0.1",
       500:"Eduardo",
       "E-mail":"nicolas.lozalml@gmail.com"
       }
print(dict1["R1"])
print(type(dict1))
dict1["S1"]="11.0.0.1"
print("R2" in dict1)




