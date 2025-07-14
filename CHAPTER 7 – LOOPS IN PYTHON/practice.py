# CHAPTER 7 – PRACTICE SET 

# 1. Write a program to print multiplication table of a given number using for loop. 
# k = int(input("Enter the number to check its multiplication table: "))
# for i in range (1,11):
#     print(f"{k} * {i} is : {i*k}")
    # print("{} * {} is: {}".format(k,i,i*k))


    
# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S. 
# l = ["Harry", "Soham", "Sachin", "Rahul"] 
# for i in l:
#     for item in i:
#         if(item[0]=="S"):
#             print(f"hello {i}")

#or
# l = ["Harry", "Soham", "Sachin", "Rahul"] 
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")

        

# 3. Attempt problem 1 using while loop. 
# l = ["Harry", "Soham", "Sachin", "Rahul"] 
# i = 0
# while i < len(l):
#     if l[i][0] == "S":
#         print(f"Hello {l[i]}")
#     i += 1



# 4. Write a program to find whether a given number is prime or not. 
# p = int(input("Enter the number: "))
# c = 0
# for i in range(1,p+1):
#     if(p % i == 0):
#         c  += 1
# if(c == 2):
#     print(f"{p} is prime number")
# else:
#     print(f"{p}Not prime")



# 5. Write a program to find the sum of first n natural numbers using while loop. 
# n = int(input("Enter the number: "))
# i=0
# s=0
# while(i<n+1):
#     s = s+i
#     i+=1
# print(f"the sum of first {n} natural number is: {s}")



# 6. Write a program to calculate the factorial of a given number using for loop.
# f = int(input("Enter the number to know its factorial: "))
# s = 1
# for i in range (1,f+1):
#     s = s*i
# print(f"the factorial of {f} is {s}")



# 7. Write a program to print the following star pattern. 
# * 
# *** 
# ***** for n = 3 
# n = int(input("Enter the number: "))
# for i in range (1 , n+1):
#     print(" "* (n-i), end="")
#     print(" * "*i, end="")
#     print("\n")



# 8. Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3 
# n = int(input("Enter the number: "))
# for i in range (1 , n+1):

#     print(" * "*i, end="")
#     print("\n")



# 9. Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * *  
# n = int(input("Enter the number: "))
# for i in range (1 , n+1):
#     if( i==1 or i==n):
#         print("*"*n, end="")
#     else:
#         print("*", end="")
#         print(" "*(n-2) , end="")
#         print("*",end="")
#     print("")


# 10. Write a program to print multiplication table of n using for loops in reversed 
# order. 
# k = int(input("Enter the number to check its multiplication table: "))
# for i in range (10,0,-1):
#     print(f"{k} * {i} is : {i*k}")
    # print("{} * {} is: {}".format(k,i,i*k))
   