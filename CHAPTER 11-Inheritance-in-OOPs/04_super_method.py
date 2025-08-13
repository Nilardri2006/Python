class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a= 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b =2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a)
# # print(o.b) #throws error

# o = Programmer()
# print(o.a , o.b)
# # print(o.c)  #throws error

o = Manager()
print(o.a, o.b, o.c)    
# Parent
#   |
#   v
# Child1
#   |
#   v
# Child2