def sort(a):
    for i in range(0, len(a)):
        for j in range(0, len(a) - 1 - i):
            if a[j] >= a[j + 1]:
                swap(a, j, j + 1)
    return a


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


print(sort([10, 11, 2, 3, 9, 5, 2, 8, 9]))
print(sort([10, 1, 2, 23, 14, 5, 6, 1, 1, 1, 1, 9]))
print(sort([0, 1, -2, 33, 4, 5, 6, 8, 9]))
print(sort([0, -2, -2, 33, 0, 5, -2, 8, -2]))
print(sort([0, 1, -2, 33, 4, 5, 6, 8, 9]))
print(sort([0, 1, -2, 33, 4, 5, 6, 8, 9]))
print(sort([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]))
print(sort([0, 1, 2, 3, 4, 5, 1, 2, 9]))
print(sort([0, 0]))
print(sort([0, -1]))
print(sort([0]))
print(sort([]))
