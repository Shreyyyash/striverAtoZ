array=[10,5,10,15,5,10]
d={}
for item in array:
    d[item]= d.get(item,0)+1
print(d)
# print(d.items())

MaxCount=0
for key,value in d.items():
    # print(key,value)
    if MaxCount<value:
        number=key
        MaxCount=value
        
print(number,MaxCount)
