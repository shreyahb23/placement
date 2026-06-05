def linear_search(ids,target):
    for i in range(len(ids)):
        if ids[i] == target:
            return i
    return -1
ids = [101,205,310,415,520]
target=310
print(linear_search(ids,target))
