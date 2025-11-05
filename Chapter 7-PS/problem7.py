n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "* (n-i),end="") # end="" it helps to not creating new line
    print("*"* (2*i-1),end="")
    print("")