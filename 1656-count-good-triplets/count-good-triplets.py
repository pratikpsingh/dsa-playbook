class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # good_triplets = []
        good_triplets = 0
        length = len(arr)

        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):

                    if (abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                        # good_triplets.append([arr[i], arr[j], arr[k]])
                        good_triplets += 1

        return good_triplets
                        

        