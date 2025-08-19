from functools import reduce

# Map
l = [1 , 2 , 3 , 4 , 5 , 6]
square = lambda x: x*x

sqList = map(square,l)
print(list(sqList))  # Output: [1, 4, 9,

#Filter
def even(n):
    if(n%2==0):
        return True
    else:
        return False
onlyEven = filter(even,l)
print(list(onlyEven))

#reduce
def sum(a,b):
    return a+b
def mul(a,b):
    return a*b
print(reduce(sum,l))
# 1+2->3+3->6+4->10+5->15+6->21
print(reduce(mul,l))
#1*2->2*3->6*4->24*5->120*6->720