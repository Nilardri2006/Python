name = "meghna"

print(len(name))#len function
print(name.endswith("na"))#checks if its true
print(name.startswith("na"))#checks if its true
print(name.capitalize())#only just capitalize the 1st letter


# ⚙️ BASIC STRING FUNCTIONS
# python
# Copy
# Edit
s = "Roney"

print(len(s))        # 5
print(str(123))      # "123"



# 🔥 CASE MODIFICATION
# python
# Copy
# Edit
s = "hello roney"

print(s.upper())         # 'HELLO RONEY'
print(s.lower())         # 'hello roney'
print(s.title())         # 'Hello Roney'
print(s.capitalize())    # 'Hello roney'



# 🧼 STRIPPING JUNK
# python
# Copy
# Edit
s = "  Roney  "

print(s.strip())     # 'Roney'
print(s.lstrip())    # 'Roney  '
print(s.rstrip())    # '  Roney'



# 🔍 FINDING STUFF
# python
# Copy
# Edit
s = "hello roney"

print(s.find("o"))       # 4 (first 'o')
print(s.index("r"))      # 6
print("ron" in s)        # True
print(s.startswith("hel"))  # True
print(s.endswith("ney"))    # True



# 🧪 CHECKING STUFF
# python
# Copy
# Edit
print("abc".isalpha())     # True
print("123".isdigit())     # True
print("abc123".isalnum())  # True
print("   ".isspace())     # True



# ✂️ SPLIT & JOIN
# python
# Copy
# Edit
s = "roney,likes,python"

print(s.split(","))           # ['roney', 'likes', 'python']

words = ['I', 'love', 'Python']
print(" ".join(words))        # 'I love Python'



# 🔄 REPLACEMENT THERAPY
# python
# Copy
# Edit
s = "I love C++"

print(s.replace("C++", "Python"))  # 'I love Python'



# 🪄 STRING FORMATTING
# python
# Copy
# Edit
name = "Roney"
lang = "Python"

# Using format()
print("My name is {} and I code in {}".format(name, lang))  
# 'My name is Roney and I code in Python'

# Using f-strings
print(f"My name is {name} and I code in {lang}")
# 'My name is Roney and I code in Python'