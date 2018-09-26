def partition(arr, first, last):
    i = first - 1
    pivot = 1

    for j in range(first, last):
        if arr[j] != pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[last] = arr[last], arr[i+1]
    return (i+1)

def quicksort(arr, first, last):
    if first < last:
        pivot = partition(arr, first, last)
        quicksort(arr, first, pivot - 1)
        quicksort(arr, pivot + 1, last)

arr = [1, 0, 0, 1, 1, 0, 0, 0, 0]
n = len(arr)
quicksort(arr, 0, n-1)
for i in arr:
    print(i)
