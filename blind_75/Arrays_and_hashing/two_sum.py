"""
# Two Sum

Easy Topics `Company Tags` Hints

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`.

You may assume that every input has exactly one pair of indices `i` and `j` that satisfy the condition.

Return the answer with the smaller index first.

**Example 1:**

```py
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
```

Explanation: `nums[0] + nums[1] == 7`, so we return `[0, 1]`.

**Example 2:**

```py
Input: nums = [4,5,6], target = 10

Output: [0,2]
```

**Example 3:**

```py
Input: nums = [5,5], target = 10

Output: [0,1]
```

**Constraints:**

- `2 <= nums.length <= 1000`
- `-10,000,000 <= nums[i] <= 10,000,000`
- `-10,000,000 <= target <= 10,000,000`
- Only one valid answer exists.

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = dict()

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in tmp:
                return [tmp[comp], i]
            tmp[nums[i]] = i
        return [-1, -1]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 4, 5, 6], 7, [0, 1]),
        ([4, 5, 6], 10, [0, 2]),
        ([5, 5], 10, [0, 1]),
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([-3, 4, 3, 90], 0, [0, 2]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([1, 3, 4, 2], 6, [2, 3]),
        ([10, -1, -9, 21], 9, [0, 1]),
        ([1, 2], 3, [0, 1]),
        ([8, 1, 2, 7], 9, [0, 1]),
        ([6, 3, 3], 6, [1, 2]),
        ([10000000, -10000000, 1], 0, [0, 1]),
        ([1, 4, 5, 11], 16, [2, 3]),
        ([-10, 20, 11, 40], 30, [0, 3]),
        ([9, 0, 1, 8], 17, [0, 3]),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 10, [1, 3]),
        ([2, 5, 5, 11], 10, [1, 2]),
        ([7, 11, 15, 2], 9, [0, 3]),
        ([-100, 50, 50], 100, [1, 2]),
        ([14, -4, 9, -5], 5, [1, 2]),
    ]

    for idx, (nums, target, expected) in enumerate(test_cases, start=1):
        result = solution.twoSum(nums, target)
        assert result == expected, (
            f"Test {idx} failed: nums={nums}, target={target}, "
            f"expected={expected}, got={result}"
        )

    print(f"All tests passed: {len(test_cases)}")
