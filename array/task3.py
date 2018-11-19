def find(a):
    if len(a) == 0:
        return None
    if len(a) == 1:
        return a[0], a[0]
    mi = a[0]
    ma = a[0]
    for i in range(1, len(a)):
        if a[i] > ma:
            ma = a[i]
        if a[i] < mi:
            mi = a[i]
    return mi, ma


print(find([0, 1, 2, 3, 4, 5, 6, 8, 9]))
print(find([0, 1, -1, 3, 4, 5, 6, 1, 9]))
print(find([0, 1, 2, 3, 10, 5, 6, 8, 9]))
print(find([0, 1, 2, 3, 4, 5, 1, 2, 9]))
print(find([0, 0]))
print(find([0, 1]))
print(find([0]))
print(find([]))
