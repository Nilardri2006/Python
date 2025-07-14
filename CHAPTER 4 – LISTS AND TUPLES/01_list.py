friends = ["apple" , "Banana" , "cherry" , "454" , "45.589" , "False"]

# print(friends[0])
friends[0] = "orange"  #unlike strings list are mutable
print(friends[0])
print(friends[1:6])

friends.append("harry")
print(friends)#not making new list but adding extra string to the list

l1= [5, 8, 5 ,9 ,4 ,6 ,2]

l1.sort()#for sorting ncreasingly
print(l1)

l1.reverse()#for sorting decreasingly
print(l1)

l1.insert(4, 55)#inserting 55 such that its index becomes 4
print(l1)

l1.pop(3)
print(l1)#removes the element at index 3

print(l1.pop(3))#removes the element at index 3 and returns it

print(l1)
value = l1.pop(3)
print(value)#removes the element at index 3 and returns it
print(l1)

value = l1.remove(9)#removes the elemnt which is written  from the list
print(l1)