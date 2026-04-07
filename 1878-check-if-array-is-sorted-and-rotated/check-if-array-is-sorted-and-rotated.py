class Solution:
    def check(self, nums: List[int]) -> bool:
        length = len(nums)
        i = 0

        while i < length - 1:
            if nums[i] <= nums[i + 1]:
                i += 1
                continue
            
            if nums[i] > nums[i + 1]:
                i += 1
                while i < length - 1:
                    if nums[i] <= nums[i + 1]:
                        i += 1
                        continue
                    else:
                        return False
                if nums[0] >= nums[length - 1]:
                    return True
                return False

        return True

        