def second_smallest(array):
    min=s_min=1515135235
    n=len(array)
    for i in range(n):
        if array[i]<min:
            s_min=min
            min=array[i]

        elif array[i]<s_min and array[i]!=min:
            s_min=array[i]     
    
    print(s_min)

array=[12, 35, 1, 10, 34, 1]
second_smallest(array)