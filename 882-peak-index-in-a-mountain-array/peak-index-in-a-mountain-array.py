class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        length = len(arr)

        start = 0
        end = length - 1

        while start <= end:
            middle = (start + end) // 2
            if middle == 0 and arr[middle] < arr[middle + 1] and arr[middle + 1] > arr[middle + 2]:
                return middle + 1

            if middle == length - 1 and arr[middle] < arr[middle - 1] and arr[middle -1] and arr[middle - 2]:
                return middle - 1

            if arr[middle] > arr[middle - 1] and arr[middle] > arr[middle + 1]:
                return middle

            if arr[middle - 1] > arr[middle] and arr[middle] > arr[middle + 1]:
                end = middle - 1

            if arr[middle - 1] < arr[middle] and arr[middle] < arr[middle + 1]:
                start = middle + 1

        return -1
        