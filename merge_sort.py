def merge(arr, first, mid, last):
    n1 = mid - first + 1
    n2 = last - mid
    # temp arrays
    l = [0]*n1
    r = [0]*n2

    for i in range(0, n1):
        l[i] = arr[i]

    for j in range(0, n2):
        r[j] = arr[mid + 1 + j]

    i = j = 0
    k = first

    while i < n1 and j < n2:
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = l[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1

def mergesort(arr, first, last):
    if first < last:
        mid = int(first + (last - first)/2)
        mergesort(arr, first, mid)
        mergesort(arr, mid + 1, last)
        merge(arr, first, mid, last)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
mergesort(arr, 0, n - 1)
for i in arr:
    print(i)
