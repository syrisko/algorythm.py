def heapify(a, i, length):
    n = i
    le = 2 * i + 1
    new_root_position = None
    if le < length -1:
        ri = 2 * i + 2
        if a[le] >= a[ri] and a[le] > a[n]:
            swap(a, n, le)
            new_root_position = le
        if a[ri] > a[le] and a[ri] > a[n]:
            swap(a, n, ri)
            new_root_position = ri
    elif a[le] > a[n]:
        swap(a, n, le)
        new_root_position = le
    return new_root_position


def heapify_full(a, length):
    for i in reversed(range(((length)// 2))):
        nrp = heapify(a, i, length)
        while nrp is not None and (2 * nrp + 2 < length or 2 * nrp + 1 < length):
            nrp = heapify(a, nrp, length)
    return a


def sort(a):
    for i in reversed(range(len(a))):
        heapify_full(a, i + 1)
        swap(a, 0, i)
    return a


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


print(sort([0, 1, 2, 3, 4, 5, 6, 7, 8]))
