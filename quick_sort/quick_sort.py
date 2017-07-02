# 思路:
# 1. 将范围内数组分割成两个部分,左边部分比中间数字小,右边部分比中间数字大
# 中间数字的位置不能固定了

# 2. 分治

# reference:
# https://pythonschool.net/data-structures-algorithms/quicksort/

import unittest


class TestPartition(unittest.TestCase):
    def test_1(self):
        array = [9, 8, 7, 6, 0, 4, 3, 2, 1, 5]
        mid_idx = partition(array, 0, len(array) - 1)
        for i in array[0:mid_idx]:
            self.assertTrue(array[i] <= array[mid_idx])

    def test_2(self):
        array = [9, 8, 7, 6, 0, 4, 3, 2, 1, 5]
        mid_idx = partition(array, 0, len(array) - 1)
        for i in array[mid_idx + 1:len(array)]:
            self.assertTrue(array[i] > mid_idx)


class TestQuicksort(unittest.TestCase):
    def test_1(self):
        array = [9, 8, 7, 6, 0, 4, 3, 2, 1, 5]
        quciksort(array, 0, len(array) - 1)
        self.assertEqual(array, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_2(self):
        array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        quciksort(array, 0, len(array) - 1)
        self.assertEqual(array, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_3(self):
        array = [3, 2, 1]
        quciksort(array, 0, len(array) - 1)
        self.assertEqual(array, [1, 2, 3])

    def test_4(self):
        array = [3]
        quciksort(array, 0, len(array) - 1)
        self.assertEqual(array, [3])

    def test_5(self):
        array = []
        quciksort(array, 0, len(array) - 1)
        self.assertEqual(array, [])


def quciksort(A, L, R):
    if L < R:
        m = partition(A, L, R)
        quciksort(A, L, m - 1)
        quciksort(A, m + 1, R)
    return A


def partition(A, L, R):
    pivot = A[L]
    left = L + 1
    right = R
    done = False
    while left <= right:
        while left <= right and A[left] <= pivot:
            left = left + 1

        while left <= right and A[right] >= pivot:
            right = right - 1

        if left <= right:
            A[left], A[right] = A[right], A[left]

    A[L], A[right] = A[right], A[L]
    return right


# def partition(A, L, R):
#     pivot = A[R]
#     left = L
#     right = R - 1
#     while left <= right:
#         while left <= right and A[left] <= pivot:
#             left = left + 1
#
#         while left <= right and A[right] >= pivot:
#             right = right - 1
#
#         if left <= right:
#             A[left], A[right] = A[right], A[left]
#
#     A[R], A[left] = A[left], A[R]
#     return left


if __name__ == '__main__':
    unittest.main()
