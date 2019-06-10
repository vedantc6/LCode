from math import ceil, floor

def k_multiply(a, b):
    if len(str(a)) == 1 or len(str(b)) == 1:
        return int(a)*int(b)
    n = max(len(str(a)), len(str(b)))
    al = a // 10**(n//2)
    ar = a % 10**(n//2)
    bl = b // 10**(n//2)
    br = b % 10**(n//2)
    p1 = k_multiply(al, bl)
    p2 = k_multiply(ar, br)
    p3 = k_multiply(al + ar, bl + br)
    return 10**(2*n//2)*p1 + 10**(n//2)*(p3 - p1 - p2) + p2

if __name__ == "__main__":
    print(k_multiply(2104, 2421))
    print(k_multiply(21, 24))
    print(k_multiply(1, 4))
