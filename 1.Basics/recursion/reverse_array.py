def reverse(array,start,end):
    while start>end:
        return
    array[start],array[end]=array[end],array[start]
    reverse(array,start+1,end-1)
    return array

array=[1,2,3,4,5]
n=len(array)
a=reverse(array,0,n-1)
print(a)

# two pointer approach

# def reverse(array):
#     n=len(array)
#     start=0
#     end=n-1
#     while start!=end:
#         array[start],array[end] = array[end],array[start]
#         start=start+1
#         end=end-1
#     return array

# swapping two numbers

# def reverse(array):
#     n=len(array)
#     for i in range(n//2):
#         array[i],array[n-i-1] = array[n-i-1],array[i]
#     return array