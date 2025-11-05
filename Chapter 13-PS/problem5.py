from functools import reduce
l=[1,5,3424,543534,65,23534,355]
def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,l))