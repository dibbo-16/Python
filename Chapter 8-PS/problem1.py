def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a=4
b=5
c=7
print("The greatest number is ", greatest(a,b,c))
