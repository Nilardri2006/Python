d = {} #empty dictionary
marks = {
    "harry" : 100,
    "sachin" : 55,
    "rahul" : 74,
     0 : "harry"
}

# print(marks.items()) #prints everything in the dictionary as a tuple
# print(marks.keys()) #print only the keys of the dictionary,ex:harry,sachin,rahul
# print(marks.values()) #prints only the values of the dictionary,ex:100,55,74

# marks.update({"sachin" : 99, "renuka" : 96}) #adds a new key-value pair to the dictionary
# print(marks) #updates the value of sachin to 99

# print(marks.get("harry")) #prints the value of the key "harry"
# print(marks.get("ronita")) #prints none because no key is present naming "ronita"

#difference between marks.get and marks[]
print(marks.get("harry2"))#prints none 
print(marks["harry2"])#throws an error because no key is present naming "harry2"


# Dictionary All-In-One Demo by Roney 🚀

# 1. Creating a dictionary
student = {
    "name": "Roney",
    "age": 20,
    "branch": "IT",
    "skills": ["C++", "HTML", "CSS"],
}

# 2. Accessing values
print("Name:", student["name"])  # Direct access
print("Age:", student.get("age"))  # Using get()

# 3. Adding or updating values
student["college"] = "Netaji Subhash Engineering College"  # Add new key
student["age"] = 21  # Update existing key
print("\nUpdated Dictionary:", student)

# 4. Deleting items
del student["branch"]  # Delete a key
removed = student.pop("skills")  # Pop a key and return its value
print("\nDeleted 'branch' and popped 'skills':", removed)

# 5. Checking for keys
if "name" in student:
    print("\n'name' exists in student dictionary")

# 6. Iterating over dictionary
print("\nIterating through dictionary:")
for key, value in student.items():
    print(f"{key} => {value}")

# 7. Dictionary length
print("\nTotal keys:", len(student))

# 8. Nested dictionary
students = {
    "101": {"name": "Roney", "age": 21},
    "102": {"name": "Souvik", "age": 22},
}
print("\nNested Dictionary Example:", students["101"]["name"])

# 9. Using dict() constructor
empty_dict = dict()
from_list = dict([("lang", "Python"), ("version", 3.10)])
print("\nFrom list of tuples:", from_list)

# 10. Copying dictionaries
copy_dict = student.copy()
print("\nCopied Dictionary:", copy_dict)

# 11. Merging dictionaries (Python 3.9+)
extra = {"hobby": "Ukulele"}
merged = student | extra
print("\nMerged Dictionary (3.9+):", merged)

# 12. Dictionary comprehension (Pythonic!)
squares = {x: x*x for x in range(5)}
print("\nDictionary Comprehension:", squares)

# 13. Using setdefault() – returns value if key exists, else adds it
default_age = student.setdefault("age", 25)  # Won't change, already exists
new_val = student.setdefault("gender", "Male")
print("\nAfter setdefault:", student)

# 14. Clearing all items
temp = student.copy()
temp.clear()
print("\nCleared Dictionary:", temp)

# 15. Getting only keys, values, and items
print("\nKeys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))


# Original dictionary
student = {
    "name": "Roney",
    "age": 21,
    "college": "Netaji Subhash Engineering College",
    "gender": "Male"
}

# 1. pop() – removes specific key and returns its value
popped_value = student.pop("age")  # Removes 'age'
print("Value popped using pop():", popped_value)
print("After pop():", student)

# 2. popitem() – removes the **last inserted** item (LIFO behavior)
last_item = student.popitem()  # Since Python 3.7, it's ordered
print("Last item popped using popitem():", last_item)
print("After popitem():", student)

# 3. del – deletes a key (no return)
del student["gender"]  # Just deletes
print("After del:", student)
