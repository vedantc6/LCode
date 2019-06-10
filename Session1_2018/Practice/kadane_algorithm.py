def kadane(a):
    max_ending_here = 0
    max_sofar = 0
    start = 0
    end = 0
    s = 0
    for i in range(len(a)):
        max_ending_here += a[i]
        if max_sofar < max_ending_here:
            max_sofar = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
    print(max_sofar)
    print(a[start:end+1])

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
kadane(arr)
