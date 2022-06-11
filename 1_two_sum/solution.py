import unittest
from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
    # declare a dictionary that will be working as memoization
    hash_map = {}
    
    # Iterate over the list
    for k, v in enumerate(numbers):
        # if target and current item difference is in dictionary:
        if target - v in hash_map.keys():
            # retrun previous item index and current item's index
            return [hash_map[target-v], k]
        else:
            # otherwise store current item and its value into the dictionary.
            hash_map[v] = k
    
    # If no item matches return negetive value list.
    return [-1, -1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(two_sum([1, 2, 3, 4, 5, 6], 9), [3,4])

    def test_case_2(self):
        nums = [11,3,4]
        self.assertEqual(two_sum(nums, 15), [0, 2])

    def test_case_3(self):
        nums = [-1,0]
        self.assertEqual(two_sum(nums, 9), [-1, -1])


if __name__ == '__main__':
    print(".....")
    unittest.main()
