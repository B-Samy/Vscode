# def linear_search(arr,key):
#     length = len(arr)

#     for i in range(length):
#         if arr[i] == key:
#             return i
        
#         return -1


# n = [2,3,4,5,6,7,7]    
# print(linear_search(n, 2))



# def binary_search(arr,key):
#     n = len(arr) - 1
#     low , high = 0, n
#     while low <=high:
#         mid = (low + high)//2
#         if arr[mid] ==key:
#             return mid

#         elif arr[mid] < key:
#             low = mid  + 1      
#         else:
#             high = mid -1
#     return -1

# number = [10,20,30,40]
# print(binary_search(number,40))





def bubble_sort(arr,key):
    n = len(arr) - 1

    low , high = 0 , n

    while low <=high:
        mid = (low + high)//2

        if arr[mid] == key:
            return mid
        elif arr[mid]<key:
            low = mid +1
        else:
            high = mid-1
    return -1


bubble_number = [2,3,3,34,23,34]
print(bubble_sort(bubble_number,23))