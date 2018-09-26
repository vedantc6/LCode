def counting_sort(arr):
    min = 9999
    max = -1
    result = len(arr)*[0]
    for i in range(len(arr)):
        if arr[i] <= min:
            min = arr[i]
        if arr[i] >= max:
            max = arr[i]

    freq_arr = (max + 1)*[0]
    for val in arr:
        freq_arr[val] += 1

    for i in range(1, len(freq_arr)):
        freq_arr[i] += freq_arr[i-1]

    for i in range(0, len(freq_arr)):
        freq_arr[i] = freq_arr[i] - 1
    # print(freq_arr)

    for val in arr:
        result[freq_arr[val]] = val
        freq_arr[val] = freq_arr[val] - 1

    return result


arr = [0, 1, 0, 0, 1, 1, 0, 0, 1, 0]
result = counting_sort(arr)
for i in result:
    print (i)
