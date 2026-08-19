class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        n=0
        while x>0:
            n=n*10+x%10
            x=x//10
        if temp == n:
            return True
        else:
            return False
        
        