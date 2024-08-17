def largest(array):
    n=len(array)
    max=array[0]
    for i in range(n):
        if array[i]>max:
            max=array[i]
    print(max)

array=[3,7,4,5,9,2,8]
largest(array)
