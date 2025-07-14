a = ("apple" , "Banana" , "cherry" , "454" , "45.589" , "False")
#a[0] = 453
# #tuples are immutable so we cannot change the value of the tuple

print(a)

no = a.count("Banana")#it says how many times the Banana occurs in the tuple
print(no)

i= a.index("454")#it gives the index of the element which is written in the bracket
print(i)


# 🔹 Tuple Basics
print("\n--- Tuple Creation ---")
my_tuple = (1, 2, 3, "hello", 3.14)
print("Tuple:", my_tuple)

# 🔸 len() - Length of tuple
print("\n--- len() ---")
print("Length:", len(my_tuple))

# 🔸 count() - Count of a value
print("\n--- count() ---")
print("Count of 3:", my_tuple.count(3))

# 🔸 index() - First index of a value
print("\n--- index() ---")
print("Index of 'hello':", my_tuple.index("hello"))

# 🔸 max(), min(), sum()
print("\n--- max(), min(), sum() ---")
numbers = (10, 20, 5, 30)
print("Numbers Tuple:", numbers)
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

# 🔸 sorted() - Returns sorted list
print("\n--- sorted() ---")
print("Sorted:", sorted(numbers))

# 🔸 all() - Are all values True?
print("\n--- all() ---")
bools = (True, 1, 3)
print("All True?:", all(bools))

# 🔸 any() - Is any value True?
print("\n--- any() ---")
flags = (False, 0, True)
print("Any True?:", any(flags))

# 🔸 tuple() - Convert to tuple
print("\n--- tuple() ---")
list_data = [1, 2, 3]
converted = tuple(list_data)
print("Converted List:", converted)

# 🔸 Concatenation
print("\n--- Concatenation ---")
a = (1, 2)
b = (3, 4)
print("a + b:", a + b)

# 🔸 Repetition
print("\n--- Repetition ---")
print("a * 3:", a * 3)

# 🔸 Membership
print("\n--- Membership ---")
print("Is 3 in b?", 3 in b)

# 🔸 Iteration
print("\n--- Iteration ---")
for item in a:
    print("Item:", item)

# 🔸 Packing
print("\n--- Packing ---")
packed = 1, "python", 3.14
print("Packed Tuple:", packed)

# 🔸 Unpacking
print("\n--- Unpacking ---")
x, y, z = packed
print("Unpacked:", x, y, z)

# 🔸 Extended Unpacking (* operator)
print("\n--- Extended Unpacking ---")
a, *b, c = (1, 2, 3, 4, 5)
print("a:", a)
print("b (rest):", b)
print("c:", c)

# 🔸 Tuples as Dictionary Keys
print("\n--- Tuples as Dict Keys ---")
point_dict = {("x", 1): "point A", ("y", 2): "point B"}
print("Value at ('x',1):", point_dict[("x", 1)])

# 🔸 Nested Tuples
print("\n--- Nested Tuples ---")
nested = (1, (2, 3), (4, (5, 6)))
print("Accessing 3:", nested[1][1])
print("Accessing 6:", nested[2][1][1])

# 🔸 Immutability (Uncomment to see error)
print("\n--- Immutability Test ---")
# my_tuple[0] = 99  # ❌ Will raise TypeError

# ✅ Done!
print("\nAll tuple operations demonstrated. You're a tuple ninja now! 🥷🔥")
