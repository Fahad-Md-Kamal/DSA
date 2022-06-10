import unittest
from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
    left , right = 0, len(numbers) -1

    while left <= right:
        sum_of_two = numbers[left] + numbers[right]
        if sum_of_two == target:
            return [left+1, right+1]
        elif sum_of_two > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        nums = [2,7,11,15]
        self.assertEqual(two_sum(nums, 9), [1, 2])

    def test_case_2(self):
        nums = [2,3,4]
        self.assertEqual(two_sum(nums, 6), [1, 3])

    def test_case_3(self):
        nums = [-1,0]
        self.assertEqual(two_sum(nums, -1), [1, 2])


if __name__ == '__main__':
    print(".....")
    unittest.main()
