def second_largest(array):
    n=len(array)
    max=array[0]
    s_max=-5352

    for i in range(n):
        if array[i]>max:
            max=array[i]
    
    for i in range(n):
        if max>array[i]>s_max and max != s_max:
            s_max=array[i]
        
    print(s_max)

array=[12, 35, 1, 10, 34, 1]
# array=[3,7,4,5,9,2,10]
second_largest(array)

# def second_largest(array):
#     n=len(array)
#     max=s_max=-31311243

#     for i in range(n):
#         if array[i]>max :
#             s_max=max
#             max=array[i]

#         elif array[i]>s_max:
#             s_max=array[i]

#     print(s_max)

# array=[12, 35, 1, 10, 34, 1]
# second_largest(array)