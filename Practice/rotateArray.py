def reverseArray(a, start, end):
    while start < end:
        temp = a[start]
        a[start] = a[end]
        a[end] = temp
        start += 1
        end -= 1


def rotateArray(arr, k):
    n = len(arr)
    reverseArray(arr, 0, k-1)
    reverseArray(arr, k, n-1)
    reverseArray(arr, 0, n-1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rotateArray(arr, 2)
    for a in arr:
        print(a)
