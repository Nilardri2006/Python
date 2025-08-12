f = open(file.txt)
print(f.read())
f.close()
# the same can also be wwiteen using with statement
with open("file.txt")as f:
    print(f.read())
    # you font need to explicityly clos file with f.close