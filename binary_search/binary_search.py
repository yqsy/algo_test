# reference: https://en.wikipedia.org/wiki/Binary_search_algorithm

# Although the idea is simple, implementing binary search correctly requires
# attention to some subtleties about its exit conditions and midpoint calculation.

import unittest



class TestBinarySearch(unittest.TestCase):
    def test_1(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(binary_search(array, 4), 4)

    def test_2(self):
        array = [0]
        self.assertEqual(binary_search(array, 0), 0)

    def test_3(self):
        array = []
        self.assertEqual(binary_search(array, 0), None)

    def test_4(self):
        array = [0, 1, 2]
        self.assertEqual(binary_search(array, 0), 0)


# test2 和 test4 说明了    while L <= R:中的=号的必要性

def binary_search(A, T):
    L = 0
    R = len(A) - 1

    while L <= R:
        m = (L + R) // 2

        if A[m] < T:
            L = m + 1

        if A[m] > T:
            R = m - 1

        if A[m] == T:
            return m

    return None


if __name__ == '__main__':
    unittest.main()
