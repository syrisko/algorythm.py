from common import swap


def merge_sort(a, aux, lo, hi):
    if lo == hi:
        return a
    mid = (lo + hi) // 2
    merge_sort(a, aux, lo, mid)
    merge_sort(a, aux, mid + 1, hi)

    i = lo
    j = mid + 1
    for ai in range(lo, hi + 1):
        if i <= mid and j <= hi:
            if a[i] > a[j]:
                aux[ai] = a[j]
                j += 1
            else:
                aux[ai] = a[i]
                i += 1
        elif i <= mid:
            aux[ai] = a[i]
            i += 1
        elif j <= hi:
            aux[ai] = a[j]
            j += 1

    for ai in range(lo, hi + 1):
        a[ai] = aux[ai]
    return a


arr = [9, 8, 9, 9, 5, 0, 3, 0, 1, 0]
aux = [0 for i in range(len(arr))]
print(merge_sort(arr, aux, 0, len(arr) - 1))
