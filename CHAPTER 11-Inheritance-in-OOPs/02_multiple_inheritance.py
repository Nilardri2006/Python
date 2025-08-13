class Employee:
    company = "ITC"
    name = "jab"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder:
    language = "python"
    def printLanguage(self):
        print(f"Out of all language ther eis your language {self.language}")
# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is{self.name} and he is good at {self.language} language")

class Programmer(Employee,Coder):  #inheriting from Employee
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good at {self.language} language")

        
a = Employee()
b = Programmer()
b.showLanguage()
b.show()

print(a.company,b.company)

# parent1  parent2
#    |        |
#     \      /
#      \   /
#       \/
#        |
#      CHILD
