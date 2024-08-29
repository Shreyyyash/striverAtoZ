def LongestSubarray(arr,target_sum):
    n=len(arr)
    count=0
    current_sum=0
    hash_map={}
    for i in range(n):
        current_sum += arr[i]
        if current_sum == target_sum:
            count = i + 1
        
        if (current_sum-target_sum) in hash_map:
            count=max(count,i- hash_map[current_sum-target_sum])
        
        if current_sum not in hash_map:
            hash_map[current_sum]=i
        
    return hash_map,count

arr=[2,3,5,1,2,3,2,2]
k=10
a=LongestSubarray(arr,k)
print(a)


# n=len(arr)
#     count=0
#     for i in range(n):
#         sum=0
#         for j in range(i,n):
#             sum=sum+arr[j]
#             if sum==k:
#                 count=max(count,j-i+1)