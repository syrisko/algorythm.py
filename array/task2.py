def find(a):
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return a[i]


print(find([0, 1, 2, 3, 4, 5, 6, 8, 9]))
print(find([0, 1, 2, 3, 4, 5, 6, 1, 9]))
print(find([0, 1, 2, 3, 4, 5, 6, 8, 9]))
print(find([0, 1, 2, 3, 4, 5, 1, 2, 9]))
print(find([0, 0]))
print(find([0, 1]))
print(find([0]))
print(find([]))
