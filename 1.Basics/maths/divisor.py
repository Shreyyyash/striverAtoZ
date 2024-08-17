def divisor(num):
    # for i in range(1,num+1):
    #     if num%i==0:
    #         print(i,end='')
    # optimized code
    
    k=1
    while k*k<=num:
        if num%k==0:
            print(k)
            if k!=num//k:  #condition for perfect square
                print(num//k)
        k=k+1
divisor(56)