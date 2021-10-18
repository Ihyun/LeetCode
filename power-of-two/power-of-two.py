class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n:
            if n==1:
                return True
            elif n%2!=0:
                return False
            n//=2
        return False