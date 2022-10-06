def dayOfYear(month,day):
    if month.lower() == 'enero':
        return day
    elif month.lower() == 'febrero':
        return 28+day
    elif month.lower() == 'marzo':
        return 59+day
    elif month.lower() == 'abril':
        return 89+day
    elif month.lower() == 'mayo':
        return 119+day
    elif month.lower() == 'junio':
        return 149+day
    elif month.lower() == 'julio':
        return 180+day
    elif month.lower() == 'agosto':
        return 211+day
    elif month.lower() == 'septiembre':
        return 241+day
    elif month.lower() == 'octubre':
        return 272+day
    elif month.lower() == 'noviembre':
        return 302+day
    elif month.lower() == "diciembre":
        return 333+day
    else:
        return 
    
year = int(input("Ingrese el año: "))
month=input('Ingrese nombre del mes: ') 
day = int(input("Ingrese el dia: "))
print(dayOfYear(month,day))


    
    