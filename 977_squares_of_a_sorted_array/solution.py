import unittest
import collections
from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
    answer = collections.deque()
    l_idx = 0
    r_idx = len(nums) -1

    while l_idx <=r_idx:
        left, right = abs(nums[l_idx]), abs(nums[r_idx])

        if left > right:
            answer.appendleft(left*left)
            l_idx += 1
        else:
            answer.appendleft(right*right)
            r_idx -= 1
    return list(answer)


class TestBinarySearch(unittest.TestCase):

    def test_case_1(self):
      self.assertEqual(sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])

    def test_case_2(self):
      self.assertEqual(sortedSquares([1, 2]), [1, 4])

    def test_case_3(self):
      self.assertEqual(sortedSquares([]), [])
    
    def test_case_4(self):
      self.assertEqual(sortedSquares([-8,-6,1,8,9]), [1,36,64,64,81])
    
    def test_case_5(self):
      self.assertEqual(sortedSquares([-1]), [1])
    
    # def test_case_5(self):
    #   self.assertEqual(sortedSquares([1, 2, 3, 4], 1), 0)
    
    # def test_case_6(self):
    #   self.assertEqual(sortedSquares([1, 2, 3, 4], 4), 3)
    
    # def test_case_7(self):
    #   self.assertEqual(sortedSquares([1, 2, 3, 4, 5, 5, 6], 6), 6)

    # def test_case_8(self):
    #   self.assertEqual(sortedSquares([1, 2, 3, 4, 5, 5, 6], 11), -1)

if __name__ == '__main__':
  unittest.main()
