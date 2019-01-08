# Write an Efficient Method to Check if a Number is Multiple of 3
def multipleOf3(n):
    odd_count = even_count = 0
    n = abs(n)
    if n == 0: return 1
    if n == 1: return 0
    while n:
        if n & 1:
            odd_count += 1
        n = n >> 1
        if n & 1:
            even_count += 1
        n = n >> 1

    return multipleOf3(abs(odd_count - even_count))

num = 24
if (multipleOf3(num)):
    print(num, 'is multiple of 3')
else:
    print(num, 'is not a multiple of 3')
