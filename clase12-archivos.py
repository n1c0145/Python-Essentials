
'''


file = open('devices.txt')
for i in file:
    i=i.strip("Cisco")
    print(i)
file.close()



'''


lista=[]
file = open('devices.txt')
for i in file:
    i=i.strip()
    lista.append(i)
    
file.close()
print(lista)
