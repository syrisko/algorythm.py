def qsort(a):
    return sort(a, 0, len(a) - 1)


def sort(a, i, j):
    if i >= j:
        return
    m = int((i + j) / 2)
    li = i
    ri = j
    while li < ri:
        while a[li] <= a[m] and li < m:
            li = li + 1
        while a[ri] >= a[m] and ri > m:
            ri = ri - 1
        if li == m:
            if ri == m:
                continue
            else:
                swap(a, li, ri)
                li = li + 1
                m = ri
        elif ri == m:
            swap(a, li, ri)
            ri = ri - 1
            m = li
        else:
            swap(a, li, ri)
            ri = ri - 1
            li = li + 1
    sort(a, i, m)
    sort(a, m + 1, j)
    return a


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


print(qsort([10, 11, 2, 3, 9, 5, 2, 8, 9]))
print(qsort([10, 1, 2, 23, 14, 5, 6, 1, 1, 1, 1, 9]))
print(qsort([0, 1, -2, 33, 4, 5, 6, 8, 9]))
print(qsort([0, -2, -2, 33, 0, 5, -2, 8, -2]))
print(qsort([0, 1, -2, 33, 4, 5, 6, 8, 9]))
print(qsort([0, 1, -2, 33, 4, 5, 6, 8, 9]))
print(qsort([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]))
print(qsort([0, 1, 2, 3, 4, 5, 1, 2, 9]))
print(qsort([0, 0]))
print(qsort([0, -1]))
print(qsort([0]))
print(qsort([]))
