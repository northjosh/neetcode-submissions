class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = list(s.lower())
        new.reverse()
        new = "".join(filter(str.isalnum, new)).replace(" ", "") 
        s = list(s.lower())
        s = "".join(filter(str.isalnum, s)).replace(" ", "") 
        return s == new



    

        