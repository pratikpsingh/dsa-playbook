class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        start = -1
        peak = -1
        max_length = 0

        for i in range(1, len(arr)):

            if arr[i] > arr[i - 1]:
                if peak != -1:
                    max_length = max(max_length, (i - 1 - start + 1))
                    peak = -1
                    start = i - 1
                    continue

                if start == -1:
                    start = i - 1
                continue
                    
            
            if arr[i] == arr[i - 1]:
                if peak != -1:
                    if peak != i - 1:
                        max_length = max(max_length, (i - 1) - start + 1)
                        peak = -1
                        start = -1
                else:
                    start = -1

                continue

            if arr[i] < arr[i - 1]:
                if start == -1:
                    continue

                if peak == -1:
                    peak = i - 1

                continue

        # if max_length == 0 and peak != -1:
        #     max_length = i - start + 1

        if peak != -1:
            max_length = max(max_length, i - start + 1)

        return max_length