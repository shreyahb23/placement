def f(x, y):
    z = x + y
    if z > 100:
        print("yes")
    else:
        print("no")
z=f(10, 20)
print(z)


def is_sum_above_limit(num1, num2, limit=100):
    total = num1 + num2

    if total > limit:
        return "Sum exceeds the limit"
    else:
        return "Sum is within the limit"

result = is_sum_above_limit(60, 50)
print(result)