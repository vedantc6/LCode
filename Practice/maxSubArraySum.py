def maxSumUsingMid(a, first, last, mid):
    max_left = -99999
    sum1 = 0
    for i in range(mid, first - 1, -1):
        sum1 += a[i]
        if sum1 > max_left:
            max_left = sum1

    max_right = -99999
    sum1 = 0
    for i in range(mid + 1, last + 1):
        sum1 += a[i]
        if sum1 > max_right:
            max_right = sum1

    return max_left + max_right

def maxSubArraySum(a, first, last):
    if first == last:
        return a[first]
    mid = (first + last)//2
    return max(maxSubArraySum(a, first, mid), maxSubArraySum(a, mid+1, last),
                maxSumUsingMid(a, first, last, mid))

arr = [-11, -5, 9, 2, 3, -2, 4, 5, 7]
n = len(arr)

max_sum = maxSubArraySum(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)
