# def NtoOne(num,i):
#     print(num)
#     while i<num:
#         return NtoOne(num-1,i)
# NtoOne(10,1)

def NtoOne(num,i):
    print(i)    # opertation before fun call
    if i<num:
        NtoOne(num,i+1)
        print(i)       # printing after recursion--> last i will print first
        
NtoOne(10,1)