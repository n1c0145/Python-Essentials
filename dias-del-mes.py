def daysInMonth(month,year):
    if month.lower() in ('enero', 'marzo', 'julio', 'agosto', 'octubre', 'diciembre'):     
        return '31'
    elif month.lower() == 'febrero':
        if year % 4 == 0 and (year % 100 != 0 or year % 400 ==0):
            return "29"
        else:
            return "28"
    else:
        return '30'
   
month = input("Ingrese el nombre del mes:")
year=int(input("Ingrese el año: "))
print(daysInMonth(month,year))