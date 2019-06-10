# You are given two arrays representing integer locations of stores and houses (each location in this problem is one-dimensional). For each house, find the store closest to it.
# For example given stores = [1, 5, 20, 11, 16] and houses = [5, 10, 17], the function should return [5, 11, 16]
# The closest store to the house at location 5 is the store at the same location
# The closest store to the house at location 10 is the store at location 11
# The closest store to the house at location 17 is the store at location 16
# M and N are integers within the range [1, 1000]
# Each element of arrays stores, houses is an integer within the range [0, 1000000]
# 1, 5, 11, 16, 20
def solution1(stores, houses):
    n = len(houses)
    m = len(stores)
    result = []*n
    for i in range(n):
        closest = 1000001
        s = 0
        for j in range(m):
            if abs(houses[i] - stores[j]) < closest:
                closest = abs(houses[i] - stores[j])
                s = stores[j]
        result.append(s)
    return result

# def binarySearch(data, val):
#     lo, hi = 0, len(data) - 1
#     best_ind = lo
#     while lo <= hi:
#         mid = lo + (hi - lo) / 2
#         if data[mid] < val:
#             lo = mid + 1
#         elif data[mid] > val:
#             hi = mid - 1
#         else:
#             best_ind = mid
#             break
#         # check if data[mid] is closer to val than data[best_ind]
#         if abs(data[mid] - val) < abs(data[best_ind] - val):
#             best_ind = mid
#     return best_ind
def solution1_binary(stores, houses):
    stores = sorted(stores)

    def binarySearch(house, stores):
        lo, hi = 0, len(stores)-1
        best_index = lo

        while lo <= hi:
            mid = (lo+hi)//2
            if stores[mid] < house:
                lo = mid + 1
            elif stores[mid] > house:
                hi = mid - 1
            else:
                best_index = mid
                break

            if abs(stores[mid] - house) < abs(stores[best_index] - house):
                best_index = mid
        return best_index

    for house in houses:
    	i,j = 0,len(stores)-1
    	print(house, stores[binarySearch(house, stores)])

# Assume you are given a tree of N nodes. The nodes are numbered from 0 to N-1 and their parents are represented in an array A, such that A[i] denotes the number of the parent of the i-th node. Node 0 is the root node and it will not have a parent, so the corresponding value in A will be -1. We define the distance between two nodes to be the length of the shortest path between them, and we define an ancestor of the i-th node as any node lying on the shortest path between the i-th node and the root. Your goal is to find the ancestor at distance D of every node of the tree.
# For example, given integer D = 2, and array A such that: A[0] = -1, A[1] = 0, A[2] = 1, A[3] = 2, A[4] = 3. Your function should return [-1, -1, 0, 1, 2]
def solution2(D, A):
    n = len(A)
    result = [0]*n

    for i in range(n):
        # print("Current index: ", i)
        temp = i
        tempD = D
        val = 0
        while tempD > 0:
            val = A[temp]
            # print("D value, Val ", tempD, val)
            if val != -1:
                temp = val
                tempD -= 1
            else: break

        # print("Final val for {} is {}".format(i, val))
        result[i] = val

    return result

def solution2_2():
    def return_parent(dic, val):
    	if val in dic:
    		return dic[val]
    	else:
    		return -1

    A = [-1, 0, 4, 2, 1]

    D = 3

    dic = {}

    new_arr = []

    for i in range(len(A)):
    	dic[i]=A[i]

    for i in range(len(A)):
    	fin = i
    	for l in range(D):
    		fin = return_parent(dic, fin)

    	new_arr.append(fin)

    print(new_arr)
# Given a string A consisting of n characters and a string B consisting of m characters, write a function that will return the number of times A must be stated such that B is a substring of the repeated A. If B can never be a substring, return -1.
# Example:
# A = ‘abcd’
# B = ‘cdabcdab’
# The function should return 3 because after stating A 3 times, getting ‘abcdabcdabcd’, B is now a substring of A.
# You can assume that n and m are integers in the range [1, 1000]
def solution3(a, b):
    i = 1
    count = 0
    while i <= 10:
        temp = a*i
        if b in temp:
            return i
        i += 1
    return -1

if __name__ == '__main__':
    print(solution1([1, 5, 20, 11, 16], [5, 10, 17]))
    solution1_binary([1, 5, 20, 11, 16], [5, 10, 17])
    print(solution2(3, [-1, 0, 4, 2, 1]))
    solution2_2()
    print(solution3('abcd', 'cdabcdab'))
