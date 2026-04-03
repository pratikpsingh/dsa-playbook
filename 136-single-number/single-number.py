class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return reduce(lambda x, y: x ^ y, nums)

        find_x = 0
        for num in nums:
            find_x ^= num

        return find_x
        