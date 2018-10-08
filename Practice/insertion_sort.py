def insertionsort(arr, first, last):
    for j in range(1, last):
        key = arr[j]
        i = j - 1
        while i > -1 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i -1
        arr[i+1] = key

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
insertionsort(arr, 0, n)
for i in arr:
    print(i)
