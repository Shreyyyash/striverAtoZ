array=[5,23,23,12,7,5,23]
d={}
for item in array:
    d[item]=d.get(item,0)+1

# for lowest frequency
MinCount=200
for key,value in d.items():
    if MinCount>value:
        number=key
        MinCount=value
print(number,MinCount)

# can use >= if they have same min count (to get last element)