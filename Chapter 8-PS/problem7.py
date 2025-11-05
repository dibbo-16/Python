def rem(list, word):
    n=[]
    for item in list:
        if not(item==word):
            n.append(item.strip(word))

    return n        

    


list=["Dibbo", "Harry", "Salman", "an"]
print(rem(list,"an"))
