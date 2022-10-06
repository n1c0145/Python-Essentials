
def isYearLeap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 ==0):
        return "Bisiesto"
    else:
        return "No es bisiesto"

year=int(input("Ingrese el año: "))
print(isYearLeap(year))









