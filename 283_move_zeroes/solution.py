import unittest
from typing import List

def moveZeroes(nums: List[int]):
    left = 0
    right = len(nums) -1

    while left <=right:

        if nums[left] == 0:
            popped_item = nums.pop(left)
            nums.append(popped_item)
            right -= 1
        else:
            left += 1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        nums = [0,-1,0,3,10]
        moveZeroes(nums)
        self.assertEqual(nums, [-1, 3, 10, 0, 0])

    def test_case_2(self):
        nums = [0, 0, 3,10]
        moveZeroes(nums)
        self.assertEqual(nums, [3, 10, 0, 0])

    def test_case_3(self):
        nums = [0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, [ 0, 0])
    
    def test_case_4(self):
        nums = []
        moveZeroes(nums)
        self.assertEqual(nums, [])
    
    def test_case_5(self):
        nums = [50, 8, 2, 0, 33, 00, 30, 20 ,4]
        moveZeroes(nums)
        self.assertEqual(nums, [50, 8, 2, 33, 30, 20, 4, 0, 00 ])

if __name__ == '__main__':
  unittest.main()
