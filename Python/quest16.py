def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        key= arr[i]
        j = i-1
        while j>=1 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

print(insertion([1,23,546,223,23,45]))