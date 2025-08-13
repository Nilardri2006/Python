class Employee:
    language = "Py"
    salary = 1200000

    def getinfo(self):
        print(f"th elanguage is {self.language} . the salary is {self.salary}")

    def greet(self):# even if u dont use self here it will also return error
        print("Good morning")

    @staticmethod #static method  is a decorator after using it it reduces the need of self, without passing object it wokrs
    def greet1():
        print("Good morning")

roney = Employee() 
roney.language = "JS" #this is an insatance attribute
print(roney.language)
roney.getinfo() #it cghanges into Employee.getinfo(roney) so it return error

#intsance attribute preference >> class attribute
# --------------------------------------------------------------
