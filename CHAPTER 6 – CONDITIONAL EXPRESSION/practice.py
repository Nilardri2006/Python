# CHAPTER 6 – PRACTICE SET 

# 1. Write a program to find the greatest of four numbers entered by the user. 
# a = int(input("enter the nummber 1: "))
# b = int(input("enter the nummber 2: "))
# c = int(input("enter the nummber 3: "))
# d = int(input("enter the nummber 4: "))

# if(a>=b and a>=c and a>=d):
#     print("{} is greatest number".format(a))
# elif(b>=a and b>=c and b>=d):
#     print("{} is greatest number".format(b))
# elif(c>=b and c>=b and c>=d):
#     print("{} is greatest number".format(c))
# else:
#     print("{} is greatest number".format(d))



# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 
# a = int(input("Enter the number got in subject 1: "))
# b = int(input("Enter the number got in subject 2: "))
# c = int(input("Enter the number got in subject 3: "))

# if((((a + b + c)/300) >= 0.4 ) and ((a/100)>=0.33) and ((b/100)>=0.33) and ((c/100)>=0.33)):
#     print("PASS")
# else:
#     print("FAIL")




# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 
# spam_keywords = [
#     "make a lot of money",
#     "buy now",
#     "subscribe this",
#     "click this"
# ]

# comment = input("enter any word to chec  spams: ".lower())

# if(comment in spam_keywords):
#     print("spam")
# else:
#     print("nope")



# 4. Write a program to find whether a given username contains less than 10 
# characters or not. 
# s = input("enter the username: ")
# if(len(s)<10):
#     print("write atleast 10 character")
# else:
#     print("ok")

# 5. Write a program which finds out whether a given name is present in a list or not. 
# s = [ "meghna" , "roney" , "debraj" ]
# p = input("the name is: ")

# if p in s :
#     print(f"{p} is present in the list")

# else:
#     print(f"{p} is not present in the list")

# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F 
# 7. Write a program to find out whether a given post is talking about “Harry” or not. 