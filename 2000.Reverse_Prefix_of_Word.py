class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        
        reverse = ""
        for i in range(len(word)):
            if word[i] == ch:
                reverse = word[:i+1]
                return reverse[::-1]+word[i+1::]
        return word