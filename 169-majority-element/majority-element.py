class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums) // 2

        uniques = dict()


        for num in nums:
            if num not in uniques:
                uniques[num] = 1
            else:
                uniques[num] += 1

        for u in uniques:
            if uniques[u] > m:
                return u