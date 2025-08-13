# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft. 
# class Programmer:

#     def __init__(self, name, salary,location,office):
#         self.name = name
#         self.salary = salary
#         self.location = location
#         self.office =office

# person1 = Programmer("Nilardri",150000000,"India","google")
# print(person1.name,person1.salary,person1.location,person1.office)
# person2 = Programmer("Nil",150000000,"Italy","google")
# print(person2.name,person2.salary,person2.location,person2.office)
# person3 = Programmer("ardri",1500,"India","google")
# print(person3.name,person3.salary,person3.location,person3.office)

#-------------------------------------------------------------------------------------------------------------------

# 2. Write a class “Calculator” capable of finding square, cube and square root of a number. 

# class Calculator:
#     def __init__(self):
#         print("hi i am Calculator")

#     def plus(self,a,b):
#         return a+b
    
#     def minus(self,a,b):
#         self.a = a
#         self.b = b
#         return a-b
    
#     def into(self,a,b):
#         return a*b
    
#     def by(self,a,b):
#         return a/b
    
# calc = Calculator()
# print(calc.plus(5,6))
# print(calc.by(5,6))

#-------------------------------------------------------------------------------------------------------------------

# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways. 
class Train:
    def __init__(self,name ,total_seats,fare):
        self.name = name
        self.total_seats = total_seats
        self.fare = fare
        self.booked_seats = 0
    
    def book_ticket(self,num_ticket):
        if self.booked_seats + num_ticket <= self.total_seats:
            self.booked_seats += num_ticket
            print(f"{num_ticket} tickets booked successfuly for {self.name}")

        else:
            print(f"Acutually NO seats are available so u cant book {num_ticket} tickets")

    def get_status(self):
        available_seats = self.total_seats - self.booked_seats
        print(f"Train: {self.name} has  Available Seats: {available_seats}, Booked Seats: {self.booked_seats}")

    def fare_info(self):
        print(f"fare for {self.name}: {self.fare} per ticket")

train1 = Train("Rajdhani", 100 , 500)
print(train1.name , train1.total_seats, train1.fare)

train1.book_ticket(30)
train1.get_status()
train1.fare_info()