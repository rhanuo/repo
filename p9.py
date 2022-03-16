class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        l = list(str(x))
        for i in range(0,int(len(l)/2)):
            if l[i] != l[-(i+1)]:
                return False
           
        return True  
