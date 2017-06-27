# reference: https://en.wikipedia.org/wiki/Binary_search_algorithm

# Although the idea is simple, implementing binary search correctly requires
# attention to some subtleties about its exit conditions and midpoint calculation.


def binary_search(A, T):
    L = 0
    R = len(A) - 1

    while L <= R:
        m = int((L + R) / 2)

        if A[m] < T:
            L = m + 1

        if A[m] > T:
            R = m - 1

        if A[m] == T:
            return m

    return -1


if __name__ == '__main__':
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    idx = binary_search(array, 4)

    print(idx)

