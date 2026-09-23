class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = list(s.lower())
        new.reverse()
        new = "".join(filter(str.isalnum, new)) 
        s = list(s.lower())
        s = "".join(filter(str.isalnum, s))
        return s == new



    

        