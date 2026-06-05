def binary_search(arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            left = mid+1
        else:
            right = mid + 1
    return -1

numbers = list(map(int,input().split))
target = int(input())
result = binary_search(numbers,target)
if result !=-1:
    print(f"Element fount at index {result}")
else:
    print("element not found")
