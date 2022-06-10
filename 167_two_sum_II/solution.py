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

    # def test_case_2(self):
    #     nums = [0, 0, 3,10]
    #     moveZeroes(nums)
    #     self.assertEqual(nums, [3, 10, 0, 0])

    # def test_case_3(self):
    #     nums = [0, 0]
    #     moveZeroes(nums)
    #     self.assertEqual(nums, [ 0, 0])
    
    # def test_case_4(self):
    #     nums = []
    #     moveZeroes(nums)
    #     self.assertEqual(nums, [])
    
    # def test_case_5(self):
    #     nums = [50, 8, 2, 0, 33, 00, 30, 20 ,4]
    #     moveZeroes(nums)
    #     self.assertEqual(nums, [50, 8, 2, 33, 30, 20, 4, 0, 00 ])

if __name__ == '__main__':
    print(".....")
    unittest.main()
