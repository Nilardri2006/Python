# class Employee:
#     a=1
#     def show(self):
#         print(f"Employee a has value:{self.a}")

# e = Employee()
# e.a = 50
# e.show()  # Output: Employee a has value:50 duse to instance attribute

# but what if i want to access the class attribute even intsnace attribute is present?
# then we use class method

class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"Employee a has value:{cls.a}")

e = Employee()
e.a = 82
e.show()# due to class method it will access class attribute