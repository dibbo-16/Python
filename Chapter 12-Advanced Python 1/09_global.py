a=89 # global vriable
def fun():
    global a # global vriable import in fun
    a=3 #local variable
    print(a)
fun() 
print(a)
   