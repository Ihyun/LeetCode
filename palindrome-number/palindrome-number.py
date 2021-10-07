class Solution:
    def isPalindrome(self, x: int) -> bool:
        strnum = str(x)
        answer = True
        lnum = len(strnum)
        for i in range((lnum)//2):
            if strnum[i]!=strnum[lnum-1-i]:
                answer = False
                break
        return answer
        