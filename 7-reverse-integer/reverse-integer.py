class Solution:
    def reverse(self, x: int) -> int:
        LOWER_BOUND = -2147483648
        UPPER_BOUND = 2147483647

        reverse_x = 0

        is_negative = False
        if x < 0:
            is_negative = True
            x = -x

        while x > 0:
            remainder = x % 10
            x //=10
            reverse_x = reverse_x * 10 + remainder

        if is_negative:
            reverse_x = -reverse_x
            if reverse_x < LOWER_BOUND:
                return 0
            return reverse_x
        if reverse_x > UPPER_BOUND:
            return 0
        return reverse_x
        
        