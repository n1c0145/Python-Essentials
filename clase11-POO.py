# -*- coding: utf-8 -*-
"""



#Poo

class MiPrimeraClase:
    pass

obj1=MiPrimeraClase()

obj2 = MiPrimeraClase()

"""


class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self,name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d", Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"      
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Sandra", 5000)
emp3 = Employee("Ana",8000)
emp4 = Employee("Briguitte",8000)
emp5 = Employee ('Juan',1200)
emp6 = Employee ('Carlos',1600)
emp7=Employee("Mirkka", 2500)
emp8=Employee(5888, 2500)
emp9=Employee("Andres", 3000)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
emp5.displayEmployee()
emp8.displayEmployee()
emp9.displayEmployee()
print ("Total Employee %d" % Employee.empCount)