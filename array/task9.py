def reverse(a):
    li = 0
    ri = len(a) - 1
    while ri > li:
        swap(a, ri, li)
        ri -= 1
        li += 1
    return a


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


print(reverse([0, 1, 2, 3, 4, 5, 6, 8, 9]))
print(reverse([0, 1, 2, 3, 4, 5, 6, 1, 9]))
print(reverse([0, 1, 2, 3, 4, 5, 6, 8, 9]))
print(reverse([0, 1, 2, 3, 4, 5, 1, 2, 9]))
print(reverse([0, 0]))
print(reverse([0, 1]))
print(reverse([0]))
print(reverse([]))
