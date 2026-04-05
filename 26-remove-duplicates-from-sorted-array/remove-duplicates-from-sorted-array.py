class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique_element = None
        swap_index = -1
        count = 0

        for index, num in enumerate(nums):
            if index == 0:
                unique_element = num
                count += 1
                continue

            if num ==  unique_element and swap_index == -1:
                swap_index = index
                continue
            elif num == unique_element and swap_index != -1:
                continue


            if num != unique_element and swap_index != -1:
                count += 1
                nums[swap_index] = num
                swap_index += 1
                unique_element = num
                continue
            elif num != unique_element and swap_index == -1:
                unique_element = num
                count += 1
                continue


        return count
                    
            



        