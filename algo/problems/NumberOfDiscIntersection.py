import unittest
# import random


RANGE_A = (0, 2147483647)
RANGE_N = (0, 100000)
MAX_INTERSECTIONS = 10000000


def slow_solution(input_array):
    """
    Brute force - visit and test every combination - O(N**2)
    56% (100% correct, 12% performance)
    """
    minimums = []
    maximums = []
    count = 0
    for i in range(len(input_array)):
        minimums.append(i - input_array[i])
        maximums.append(i + input_array[i])

    for i in range(len(maximums)):
        for j in range(i + 1, len(minimums)):
            if maximums[i] >= minimums[j]:
                count += 1
    return count


def fast_solution(input_array):
    """
    Simplified solution - O(N*Log(N))
    56% (100% correct, 12% performance)
    """
    maximums = []
    minimums = []
    count = 0
    for i in range(len(input_array)):
        maximums.append(i + input_array[i])
        minimums.append(i - input_array[i])
    maximums.sort()
    minimums.sort()
    j = 0
    for i in range(len(maximums)):
        while j < len(minimums) and maximums[i] >= minimums[j]:
            j += 1
        count += j - i - 1
        if count > 10000000:
            return -1
    return count


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([1, 5, 2, 1, 4, 0]), 11)

    def test_simple(self):
        self.assertEqual(solution([1, 1, 1]), 3)  # this is not 5, but 3!

    def test_extreme_small(self):
        self.assertEqual(solution([]), 0)
        self.assertEqual(solution([10]), 0)
        self.assertEqual(solution([1, 1]), 1)

    def test_extreme_large(self):
        arr = [10000000] * 100000
        self.assertEqual(solution(arr), -1)


solution = fast_solution

if __name__ == '__main__':
    unittest.main()
