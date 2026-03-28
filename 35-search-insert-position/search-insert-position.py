class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)


        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if target > nums[middle]:
                left = middle + 1

            if target < nums[middle]:
                right = middle -1

        return left



    