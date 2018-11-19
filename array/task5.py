def find(a):
    res = set()
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                res.add(a[i])
    if len(res) > 0:
        return res
    return None


print(find([0, 1, 2, 3, 9, 5, 2, 8, 9]))
print(find([0, 1, 2, 3, 4, 5, 6, 1, 1, 1, 1, 9]))
print(find([0, 1, 2, 3, 4, 5, 6, 8, 9]))
print(find([0, 1, 2, 3, 4, 5, 1, 2, 9]))
print(find([0, 0]))
print(find([0, 1]))
print(find([0]))
print(find([]))
