"""
# Contains Duplicate


Given an integer array `nums`, return `true` if any value appears more than once in the array, otherwise return `false`.

**Example 1:**

```python
Input: nums = [1, 2, 3, 3]

Output: true
```

**Example 2:**

```python
Input: nums = [1, 2, 3, 4]

Output: false
```

**Constraints:**

`0 <= nums.length <= 10^5`
`-10^9 <= nums[i] <= 10^9`
"""

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp_set = set()
        for n in nums:
            if n in tmp_set:
                return True
            tmp_set.add(n)
        return False
        
        
        

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 3], True),
        ([1, 2, 3, 4], False),
        ([], False),
        ([-1, -2, -3, -1], True),
        ([10], False),
    ]

    for idx, (nums, expected) in enumerate(test_cases, start=1):
        result = solution.hasDuplicate(nums)
        assert result == expected, (
            f"Test {idx} failed: nums={nums}, expected={expected}, got={result}"
        )

    print(f"All tests passed: {len(test_cases)}")
