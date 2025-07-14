# PROPERTIES OF SETS 
# 1. Sets are unordered => Element’s order doesn’t matter 
# 2. Sets are unindexed => Cannot access elements by index 
# 3. There is no way to change items in sets. 
# 4. Sets cannot contain duplicate values. 

s = {1, 5 , 32 , 54 , "Harry" , 1.5 , (1, 2, 3) , True}

print(s , type(s))

s.add(566) #adds 566 to the set
print(s)
s.remove(1) #removes 1 from the set
print(s)

# Python Set Methods - All in One Place

# Creating sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {7, 8}

# 1. add(): Adds a single element
set1.add(10)
print("After add:", set1)

# 2. update(): Adds multiple elements (from any iterable)
set1.update([11, 12])
print("After update:", set1)

# 3. remove(): Removes element, raises error if not found
set1.remove(10)
print("After remove:", set1)

# 4. discard(): Removes element if found; no error if not found
set1.discard(100)  # No error
print("After discard:", set1)

# 5. pop(): Removes and returns a random element
popped = set1.pop()
print("After pop:", set1, "| Popped element:", popped)

# 6. clear(): Empties the set
temp_set = set1.copy()
temp_set.clear()
print("After clear:", temp_set)

# 7. copy(): Shallow copy of set
copied_set = set2.copy()
print("Copied set:", copied_set)

# 8. union(): Combines sets (can use | as shorthand)
print("Union:", set1.union(set2))
print("Union (|):", set1 | set2)

# 9. intersection(): Common elements (can use &)
print("Intersection:", set1.intersection(set2))
print("Intersection (&):", set1 & set2)

# 10. difference(): Elements in set1 but not in set2 (can use -)
print("Difference:", set1.difference(set2))
print("Difference (-):", set1 - set2)

# 11. symmetric_difference(): Elements in either set but not both (^)
print("Symmetric Difference:", set1.symmetric_difference(set2))
print("Symmetric Difference (^):", set1 ^ set2)

# 12. isdisjoint(): True if sets have no elements in common
print("Is Disjoint (set1 & set3):", set1.isdisjoint(set3))

# 13. issubset(): True if all elements of set1 are in set2 (<=)
print("Is Subset:", {3, 4}.issubset(set2))

# 14. issuperset(): True if set2 has all elements of another set (>=)
print("Is Superset:", set2.issuperset({3, 4}))

# 15. intersection_update(): Updates set1 with common elements
setA = {1, 2, 3}
setB = {2, 3, 4}
setA.intersection_update(setB)
print("After intersection_update:", setA)

# 16. difference_update(): Removes common elements from set1
setC = {1, 2, 3}
setD = {2, 3, 4}
setC.difference_update(setD)
print("After difference_update:", setC)

# 17. symmetric_difference_update(): Keep only non-common elements
setE = {1, 2, 3}
setF = {3, 4, 5}
setE.symmetric_difference_update(setF)
print("After symmetric_difference_update:", setE)
