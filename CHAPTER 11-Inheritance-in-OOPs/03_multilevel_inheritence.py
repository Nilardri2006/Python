class Employee:
    a= 1

class Programmer(Employee):
    b =2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)
# print(o.b) #throws error

o = Programmer()
print(o.a , o.b)
# print(o.c)  #throws error

o = Manager()
print(o.a, o.b, o.c)    
# Parent
#   |
#   v
# Child1
#   |
#   v
# Child2