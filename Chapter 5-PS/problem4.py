s=set()
#1==1.0 are same.it will not differentiate because of datatype
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))