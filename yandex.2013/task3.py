# def sum(size, s, f, b):
#     arr = [0 for i in range(size)]
#     for i in range(b):
#         for j in reversed(range(size-1)):
#             if arr[j] != 0 and arr[j] >= arr[j+1]:
#                 arr[j] -= 1
#                 arr[j+1] += 1
#         arr[0] += 1
#     res = 0
#     for i in range(s-1,f):
#         res += arr[i]
#     return res


def sum(size, s, f, b):
    res = 0
    if b <= size:
        res = f - s + 1
    else:
        l = b // size
        n = b % size
        res = (f - s + 1) * l
        in_range = size - n + 1 - s
        if in_range >= 0:
            res += (f + n - size)
    return res


print(sum(10, 10, 10, 11))
print(sum(10, 1, 10, 100))
print(sum(1000000000000, 1, 1234, 412412314))
print(sum(1000000000000, 1, 1234, 412412314))
print(sum(1000000000000, 1, 1234, 412412314))
