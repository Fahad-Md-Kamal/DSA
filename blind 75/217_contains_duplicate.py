class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        temp_dict = {}
        for n in nums:
            if temp_dict.get(n, None):
                return True
            else:
                temp_dict[n] = True
        return False
    

res = Solution().containsDuplicate([0,4,5,0,3,6])
print(res)