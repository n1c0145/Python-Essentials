
#Condicional if

datos =1
nativa =100

if datos==nativa:
    print('Los valores son iguales')
else:
    print("Los valores son diferentes")
    

#elif

acl=int(input('Ingrese el numero de acl'))


if acl>=1 and acl <=99:
    print("Acl tipo estandar")
elif acl>=100 and acl<=199:
    print("Acl extendida")
else:
    print("No es acl")