def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]


    return arr


arr = [2,3,23,12,34,56,8,1,34]
print(f"Ogi Array {arr}")

sorted = bubble_sort(arr)
print(f"Sorted array {sorted}")