arr = [10,20,30,40,50]
print("traversing an array")
for i in range(len(arr)):
    print(f"Index {i} :  {arr[i]}")

arr=[20,50,10,40,30]
print("sorting an array")
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)

arr = [9.7,3.2,6.0,7.1]
print("sorting an array")
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)