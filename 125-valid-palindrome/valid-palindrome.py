class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # if s.strip() == '' or len(s) == 1:
        #     return True

        # i = 0 
        # j = len(s) - 1
        # valid_chars = set('abcdefghijklmnopqrstuvwxyz1234567890')
        # while i <= j:
        #     while s[i] not in valid_chars:
        #         i += 1
        #         if i == len(s):
        #             return True
        #     while s[j] not in valid_chars:
        #         j -= 1
        #         if j == i:
        #             return True

        #     if i == j:
        #         return True

        #     if s[i] == s[j]:
        #         i += 1
        #         j -= 1
        #     else:
        #         return False

        # return True


        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True