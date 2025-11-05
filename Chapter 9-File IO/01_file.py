'''
Notes:
when program run, it loads in memory.here memory is RAM
RAM= Random Access Memory
Ram= Volatile
HDD(hard disk, pendripe,ssd)= Not Volatile
persist= save

'''

f=open("file.txt","r")
data=f.read()
print(data)
f.close()