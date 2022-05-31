import unittest


def binary_search(arr, target):
  left_idx = 0
  right_idx = len(arr)-1

  while left_idx <= right_idx:
    mid = left_idx + (right_idx - left_idx) // 2

    if arr[mid] == target:
      return mid

    elif target < arr[mid]:
      right_idx = mid-1

    else:
      left_idx = mid+1

  return -1


class TestBinarySearch(unittest.TestCase):

    def test_case_1(self):
      self.assertEqual(binary_search([], 3), -1)

    def test_case_2(self):
      self.assertEqual(binary_search([1, 2], 3), -1)

    def test_case_3(self):
      self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)
    
    def test_case_4(self):
      self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
    
    def test_case_5(self):
      self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)
    
    def test_case_5(self):
      self.assertEqual(binary_search([1, 2, 3, 4], 1), 0)
    
    def test_case_6(self):
      self.assertEqual(binary_search([1, 2, 3, 4], 4), 3)
    
    def test_case_7(self):
      self.assertEqual(binary_search([1, 2, 3, 4, 5, 5, 6], 6), 6)

    def test_case_8(self):
      self.assertEqual(binary_search([1, 2, 3, 4, 5, 5, 6], 11), -1)

if __name__ == '__main__':
  unittest.main()

  # pytest -q 704_binary_search/binary_search.py