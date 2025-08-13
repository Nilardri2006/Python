class Employee:
    language = "Py"
    salary = 1200000

    def __init__(self,name,salary,language): #dunder method it automatically called only init dunder method is auto called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating a object")

    def getinfo(self):
        print(f"th elanguage is {self.language} . the salary is {self.salary}")



    @staticmethod
    def greet1():
        print("Good morning")

roney = Employee("Nilardri Pramanick",1500 ,"lulu") 
# roney.name = "ZooZoo"
print(roney.name,roney.salary)
