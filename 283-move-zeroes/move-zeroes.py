class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = -1
        for index, num in enumerate(nums):
            if num == 0 and zero_index == -1:
                zero_index = index
                continue

            if num != 0 and zero_index != -1:
                nums[zero_index] = num
                nums[index] = 0 
                zero_index += 1
            


        

        
        