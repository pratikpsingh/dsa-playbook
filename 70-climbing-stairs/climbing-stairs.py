class Solution:
    def climbStairs(self, n: int) -> int:
        # if n ==1:
        #     return 1

        # if n == 0:
        #     return 1

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        count = [1, 1]
        for i in range(2, n + 1):
            count.append(count[i - 1] + count[i - 2])
        return count[-1]

