def isPalindrome(self, x: int) -> bool:
        if x <= 0:
            return False
        str_x = str(x)
        rev_x = str_x[::-1]
        if str_x == rev_x:
            return True
        return False