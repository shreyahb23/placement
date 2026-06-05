# O(1) constants time complexity
def get_first(arr):
    return arr[0]

# O(n) linear time complexity
def print_all(arr):
    for item in arr:
        print(item)

# O(n^2) quadratic time complexity
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)