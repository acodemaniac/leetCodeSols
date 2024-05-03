class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #Approach 1

        y = str(x)
        if y[::-1] == str(x):
            return True
        
        #Approach 2
        
        num = x
        rev = 0
        original = num
        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num //= 10
        return rev == original