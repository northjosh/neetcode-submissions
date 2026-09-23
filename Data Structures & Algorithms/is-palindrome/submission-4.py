class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()

        while left < right:
            if(not str.isalnum(s[left])):
                left+=1
                continue
            
            if(not str.isalnum(s[right])):
                right-=1
                continue

            
            if(s[left] != s[right]):
                return False
            else:
                left+=1;
                right-=1;
        
        return True

    

        