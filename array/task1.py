def find(a, i, j):
    if i == j:
        if i != a[i]:
            return i
        return None
    k = int((i + j) / 2)
    if k < a[k]:
        return find(a, i, k)
    else:
        return find(a, k + 1, j)


array = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
print(find(array, 0, len(array) - 1))
