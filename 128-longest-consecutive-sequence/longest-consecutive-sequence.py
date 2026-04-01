class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     unique_nums = dict()

    #     for num in nums:
    #         unique_nums[num] = False

    #     max_band_length = 0
    #     for num in nums:

    #         if unique_nums[num]:
    #             continue

    #         band_start = num
    #         band_end = num
    #         temp = num - 1
    #         while True:
    #             if temp in unique_nums:
    #                 band_start = temp
    #                 temp -= 1
    #             else:
    #                 break
    #         temp = num + 1
    #         while True:
    #             if temp in unique_nums:
    #                 band_end = temp
    #                 temp += 1
    #             else:
    #                 break

    #         max_band_length = max(max_band_length, band_end - band_start + 1)
                
    #     return max_band_length

    def longestConsecutive(self, nums: List[int]) -> int:
        unique_set = set(nums)
        unique_list = list(unique_set)


        max_band_length = 0

        for num in unique_list:
            if num - 1 in unique_set:
                continue

            count = 1
            temp = num + 1
            while True:
                if temp in unique_set:
                    count += 1
                    temp +=1 
                else:
                    break

            max_band_length = max(max_band_length, count)
        
        return max_band_length
                



































