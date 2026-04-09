class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        n0 = 0
        n1 = 1
        for i in range(2, n + 1):
            fn = n0 + n1
            n0 = n1
            n1 = fn

        return fn


        