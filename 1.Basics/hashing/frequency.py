array=[10,5,10,15,5,10]
d={}
for item in array:
    d[item] = d.get(item,0)+1
print(d)


# dic={'yash':10,'shreaysh':12,'harsh':14}
# print( dic['yash'] , dic.get('yash'))
# print(dic['yash'])