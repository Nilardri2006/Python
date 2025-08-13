class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"Employee a has value:{cls.a}")

    @property 
    def name(self): 
        return f"{self.fname} {self.lname}"
    
    @name.setter    
    def name (self,value): 
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 82

e.name = "John Doe"  # This will raise an AttributeError since 'ename' is not defined
print(e.name)

e.show()