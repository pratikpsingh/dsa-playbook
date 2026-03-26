class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()

        for i in range(len(nums)):
            x = target - nums[i]
            if x in s:
                return [s[x], i]
            s[nums[i]] = i

        return [-1, -1]