class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        index_left = 0
        index_right = len(numbers) - 1

        while (index_left < index_right):
            current_sum = numbers[index_left] + numbers[index_right]
            if current_sum == target:
                return [index_left + 1, index_right + 1]

            if current_sum < target:
                index_left += 1

            if current_sum > target:
                index_right -= 1

        return [0, 0]
        