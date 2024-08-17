def OneToN(num,i):
    print(i)   
    while i<num:
        return OneToN(num,i+1) 
    # print(i)
    # if i<num:
    #     OneToN(10,i+1)       

OneToN(10,1)