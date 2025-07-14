# CHAPTER 5 – PRACTICE SET 
# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 

# hindi_to_english = {
#     "kuttaa": " Dog ",
#     "billi": " Cat ",
#     "ghar": " House ",
#     "paani": " Water ",
#     "roti": " Bread ",
#     "doodh": " Milk ",
#     "aadmi": " Man ",
#     "aurat": " Woman ",
#     "ladka": " Boy ",
#     "ladki": " Girl ",
#     "gaadi": " Car ",
#     "kitab": " Book ",
#     "kursi": " Chair ",
#     "mez": " Table ",
#     "darwaza": " Door ",
#     "khidki": " Window ",
#     "ped": " Tree ",
#     "phool": " Flower ",
#     "aag": " Fire ",
#     "aasmaan": " Sky "
# }
# print("Welcome to Hindi to English Dictionary!")
# a = input("Enter any word in hindi to know its english meaning:  ")
# print("English meaning of {} is:{}" .format(a , hindi_to_english[a]))




# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 
# print("enter 8 numbers on by one with enter key")
# a = int(input(" "))
# b = int(input(" "))
# c = int(input(" "))
# d = int(input(" "))
# e = int(input(" "))
# f = int(input(" "))
# g = int(input(" "))
# h = int(input(" "))

# s1 ={ a , b , c , d , e , f, g , h } #making a set
# print(s1)# succesfully  printed each number once



# 3. Can we have a set with 18 (int) and '18' (str) as a value in it? 

#yes sir!
# s = { 18 , "18" }
# print( s , type(s))



# 4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 
# print(len(s))

# Sets in Python use hashing and equality to determine uniqueness.

# So when you do s.add(20.0) after s.add(20), Python checks:

# “Hey, is 20.0 equal to anything already in the set?”

# And since it sees 20 is already there and 20 == 20.0, it skips adding it. resulting length 2 for 1 20.0 and "20"




# 5. s = {} 
# What is the type of 's'? 
# s = {} 
# print(type(s)) # <class 'dict'>




# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 
# a = input("enter daksh your fav language as the value: ")
# b = input("enter dakshna your fav language as the value: ")
# c = input("enter dakshi your fav language as the value: ")
# d = input("enter daksho your fav language as the value: ")

# friends_fav_lang = {
#     "daksh": a,
#     "dakshna": b,
#     "dakshi": c,
#     "daksho": d
# }

# print(friends_fav_lang)


# 7. If the names of 2 friends are same; what will happen to the program in problem  6? 
# a = input("enter daksh your fav language as the value: ")
# b = input("enter dakshna your fav language as the value: ")
# c = input("enter dakshi your fav language as the value: ")
# d = input("enter daksho your fav language as the value: ")

# friends_fav_lang = {
#     "daksh": a,
#     "daksh": b, ## This will overwrite the previous value for "daksh" what  will result to reduce a value from  the dictionary
#     "dakshi": c,
#     "daksho": d
# }

# print(friends_fav_lang)



# 8. If languages of two friends are same; what will happen to the program in problem 
# 6? 

# a = input("enter daksh your fav language as the value: ")
# b = input("enter dakshna your fav language as the value: ")
# c = input("enter dakshi your fav language as the value: ")
# d = input("enter daksho your fav language as the value: ")

# friends_fav_lang = {
#     "daksh": a,
#     "dakshna": b, #no change will happen in thsi case because it is spossible for keeping same language value for different keys
#     "dakshi": c,
#     "daksho": d
# }

# print(friends_fav_lang)




# 9. Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 
# a list which is contained in set S?
# IndentationError: unexpected indent
# instead we need  to use tuple inside the set
# s = {8, 7, 12, "Harry", (1,2)} 
# even though its not possible to edit a tuple inside a set as tuples are immutable so answer is not possible