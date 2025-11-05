def divisible5(n):
    if(n%5==0):
        return True
    return False    
a=[1,5,34324,543534,65,23534,355]
f=list(filter(divisible5,a))
print(f)