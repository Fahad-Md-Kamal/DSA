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

    nums = [1, 2, 3, 3]
    print(solution.hasDuplicate(nums))  # Output: true

    nums = [1, 2, 3, 4]
    print(solution.hasDuplicate(nums))  # Output: false
