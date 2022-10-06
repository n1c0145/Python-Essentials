
#Errores

try:
    print("1")
    x=1/0
    print("2")
except:
    print("Salio mal")
print("3")


try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")
print("THE END.")



try:
    y=1/0
except ZeroDivisionError:
        print("Zero problem")
except ArithmeticError:
    print("Aritmetic problem")
print("The end")