class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        temp_dict = {}

        for idx, val in enumerate(nums):
            if val in temp_dict.keys():
                return [temp_dict[val], idx]
            temp_dict[target - val] = idx
        return [-1, -1]
    
rl = Solution().twoSum([2,7,11, 15], 26)
print(rl)