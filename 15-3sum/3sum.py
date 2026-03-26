class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        target = 0
        nums.sort()

        result = []
        unique_s = set()

        for i in range(len(nums) - 2):
            value = nums[i]
            remaining = target - value

            j = i + 1
            k = len(nums) - 1

            while j < k:
                temp = nums[j] + nums[k]
                if temp == remaining:
                    s = str(value) + str(nums[j]) + str(nums[k])
                    if s not in unique_s:
                        result.append([value, nums[j], nums[k]])
                    unique_s.add(s)
                    j += 1
                    k -= 1
                
                if temp < remaining:
                    j += 1

                if temp > remaining:
                    k -= 1

                
        return result
        