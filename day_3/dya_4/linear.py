def linear_search(arr , target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [10,25,37,42,58]
print(linear_search(arr,37))
arr.insert(4,45)
print("Inserted array:",arr)
arr.remove(10)
print("deleted arra :",arr)