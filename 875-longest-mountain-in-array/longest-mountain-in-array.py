class Solution:

    # Method 01
    # def longestMountain(self, arr: List[int]) -> int:
    #     start = -1
    #     peak = -1
    #     max_length = 0

    #     for i in range(1, len(arr)):

    #         if arr[i] > arr[i - 1]:
    #             if peak != -1:
    #                 max_length = max(max_length, (i - 1 - start + 1))
    #                 peak = -1
    #                 start = i - 1
    #                 continue

    #             if start == -1:
    #                 start = i - 1
    #             continue
                    
            
    #         if arr[i] == arr[i - 1]:
    #             if peak != -1:
    #                 if peak != i - 1:
    #                     max_length = max(max_length, (i - 1) - start + 1)
    #                     peak = -1
    #                     start = -1
    #             else:
    #                 start = -1

    #             continue

    #         if arr[i] < arr[i - 1]:
    #             if start == -1:
    #                 continue

    #             if peak == -1:
    #                 peak = i - 1

    #             continue

    #     # if max_length == 0 and peak != -1:
    #     #     max_length = i - start + 1

    #     if peak != -1:
    #         max_length = max(max_length, i - start + 1)

    #     return max_length

        # Method 02
        def longestMountain(self, arr: List[int]) -> int:
            # Find all picks and find the length
            longest_mountain = 0
            i = 1
            n = len(arr)
            while i < n - 1:
                count = 0
                if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                    j = i
                    count = 1 # for peak -> count peak
                    while j > 0 and arr[j] > arr[j - 1]:
                        count += 1
                        j -= 1

                    j = i
                    while i < n - 1 and arr[i] > arr[i + 1]:
                        count += 1
                        i += 1

                    longest_mountain = max(longest_mountain, count)
                else:
                    i += 1

            return longest_mountain





























