class Solution:
    def check(self, nums: List[int]) -> bool:
        # length = len(nums)
        # i = 0

        # while i < length - 1:
        #     if nums[i] <= nums[i + 1]:
        #         i += 1
        #         continue
            
        #     if nums[i] > nums[i + 1]:
        #         i += 1
        #         while i < length - 1:
        #             if nums[i] <= nums[i + 1]:
        #                 i += 1
        #                 continue
        #             else:
        #                 return False
        #         if nums[0] >= nums[length - 1]:
        #             return True
        #         return False

        # return True


        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
            if count > 1:
                return False

        return True
        