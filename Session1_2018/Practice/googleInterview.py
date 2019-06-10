def solution(S, E):
    S.sort()
    E.sort()
    chair = 0
    result = 1
    i, j = 1, 0
    n = len(S)

    while i < n and j < n:
        if S[i] <= E[j]:
            chair += 1
            i += 1

            if chair > result:
                result = chair

        else:
            chair -= 1
            j += 1
    return result

if __name__ == '__main__':
    S = [1, 2, 6, 5, 3]
    E = [5, 5, 7, 6, 8]
    print(solution(S, E))
