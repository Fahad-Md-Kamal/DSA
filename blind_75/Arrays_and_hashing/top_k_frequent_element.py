# https://neetcode.io/problems/top-k-elements-in-list/question?list=blind75

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        bucket = [[] for i in range(len(nums)+1)]
        for key, val in freq.items():
            bucket[val].append(key)
        
        result = []
        for count in range(len(bucket)-1, 0, -1):
            for num in bucket[count]:
                result.append(num)   
                if len(result) == k:
                    return result
        return result
        
        
def matches_expected(actual: List[int], expected: List[int]) -> bool:
    return len(actual) == len(expected) and set(actual) == set(expected)     

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([7, 7, 7, 7, 4, 4, 4, 6, 6], 2, [7, 4]),
        ([-1, -1, -1, -2, -2, -3], 1, [-1]),
        ([5, 5, 6, 6, 6, 7], 2, [6, 5]),
    ]

    for idx, (nums, k, expected) in enumerate(test_cases, start=1):
        result = solution.topKFrequent(nums, k)
        assert matches_expected(result, expected), (
            f"Test {idx} failed: nums={nums}, k={k}, "
            f"expected={expected}, got={result}"
        )

    print(f"All tests passed: {len(test_cases)}")
