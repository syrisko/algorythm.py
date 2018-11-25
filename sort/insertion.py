def insertionSort1(arr):
    for i in range(1,len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
                print('stop')
        # if i > 0:
        print(arr)

print(insertionSort1([1, 4, 3, 5, 6, 2]))