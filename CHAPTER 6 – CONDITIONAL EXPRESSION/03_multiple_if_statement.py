a = int(input("Enter your age: "))


#if statement no. 1
if(a%2==0):
    print("a is an even age")
#end of if stement no 1

# multiple if statement will work isolately but one by one

#if statement no. 2
if(a>=18) :
    print("You are above the age of consent")
    print("Good For u")

elif(a<0):
    print("Tu thora sa dhila hai kya?")

elif(a==0):
    print("This is valid age though")

else: 
    print("You are below the age of consent")
#end of if stement no 2
