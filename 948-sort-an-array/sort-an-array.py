class Solution:
    def merge_sort(self, list1: List[int], list2: List[int]) -> List[int]:
        index_l1: int = 0
        index_l2: int = 0

        sorted_list: List[int] = []

        while True:
            if index_l1 >= len(list1) and index_l2 < len(list2):
                while index_l2 < len(list2):
                    sorted_list.append(list2[index_l2])
                    index_l2 += 1
                break

            if index_l2 >= len(list2) and index_l1 < len(list1):
                while index_l1 < len(list1):
                    sorted_list.append(list1[index_l1])
                    index_l1 += 1
                break

            if list1[index_l1] <= list2[index_l2]:
                sorted_list.append(list1[index_l1])
                index_l1 += 1
            else:
                sorted_list.append(list2[index_l2])
                index_l2 += 1

        return sorted_list

    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        index_middle = len(nums) // 2

        list1 = self.sortArray(nums[:index_middle])
        list2 = self.sortArray(nums[index_middle:])

        return self.merge_sort(list1, list2)

        