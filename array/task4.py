def find(a, expected):
    result = []
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == expected:
                result.append((a[i], a[j]))
    return result


print(find([0, 1, 2, 3, 4, 5, 6, 8, 9], 5))
print(find([0, 1, 2, 3, 4, 5, 6, 1, 9], 7))
print(find([0, 1, 2, 3, 4, 5, 6, 8, 9], 4))
print(find([0, 1, 2, 3, 4, 5, 1, 2, 9], 2))
print(find([0, 0], 2))
print(find([0, 1], 1))
print(find([0], 0))
print(find([], 0))
