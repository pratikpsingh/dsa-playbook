class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0
        count_ones = 0
        for num in nums:
            if num == 0:
                max_consecutive_ones = max(max_consecutive_ones, count_ones)
                count_ones = 0

            if num == 1:
                count_ones += 1

        return max(max_consecutive_ones, count_ones)
            
        