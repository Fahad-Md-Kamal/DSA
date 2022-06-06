import unittest
from typing import List

def rotate(nums: List[int], k: int) -> None:
    l_idx = 0
    r_idx = len(nums) -1

    while l_idx <= r_idx and k > 0:
        right_items = nums.pop()
        nums.insert(0, right_items)
        k -=1


class TestBinarySearch(unittest.TestCase):

    def test_case_1(self):
        nums = [-4, -1, 0, 3, 10]
        rotate(nums, 2)
        self.assertEqual(nums, [3, 10, -4, -1, 0])

    # def test_case_2(self):
    #   self.assertEqual(rotate([1, 2], 1), [2, 1])

    # def test_case_3(self):
    #   self.assertEqual(rotate([], 0), [])
    
    # def test_case_4(self):
    #   self.assertEqual(rotate([-8, -6, 1, 8, 9], 4), [-6, 1, 8, 9, -8])
    
    # def test_case_5(self):
    #   self.assertEqual(rotate([-1], 0), [-1])
    
if __name__ == '__main__':
  unittest.main()
