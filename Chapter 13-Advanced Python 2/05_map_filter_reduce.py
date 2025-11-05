from functools import reduce
l=[1,2,3,4,5]
# Map example
square =lambda x: x*x

sqList= map(square,l)
# print(sqList) # output: <map object at 0x00000287E53801C0>
print(list(sqList))

# Filter example
def even(n):
    if(n%2==0):
        return True
    return False
onlyEven= filter(even,l)
print(list(onlyEven))

#Reduce example

def sum(a,b):
    return a+b
mul= lambda x,y:x*y

print(reduce(sum,l)) # 1st 2 add,then that ans with third one add.process going on the same way
print(reduce(mul,l)) # 1st 2 mul,then that ans with third one mul.process going on the same way


