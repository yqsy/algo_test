def divid(L, R):
    if L < R:
        m = (L + R) // 2
        print('%s %s %s' % (L, m, R))
        divid(L, m)
        divid(m + 1, R)


def quick_sort(A):
    divid(0, len(A) - 1)


if __name__ == '__main__':
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    quick_sort(array)
