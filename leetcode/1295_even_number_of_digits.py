# def get_digit_len(num):
#     return len(str(abs(num)))

# def odd_even_check(val):
#     return get_digit_len(val)%2 == 0

# def even_number_check(arr:list):
#     res = 0
#     for i in range(len(arr)):
#         if odd_even_check(arr[i]):
#             res += 1
#     return res


def even_number_check(nums:list):
    res = 0
    for i in range(len(nums)):
        if len(str(abs(nums[i])))%2 == 0:
            res += 1
    return res


# print(even_number_check([12, 345, 2, 6, 7896]))

class Solution:
    """
    Solution with sum()
    """
    def findNumbers(self, nums: list) -> int:
        return sum((len(str(i))) % 2 == 0 for i in nums)

class Solution:
    """
    Solution with lambda & map()
    """
    def findNumbers(self, nums: list) -> int:
        return sum(map(lambda x: 1 if len(str(x)) % 2 == 0 else 0, nums))


# print(Solution().findNumbers([12, 345, 2, 6, 7896]))


