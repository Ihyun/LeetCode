class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = ''
        
        i = len(s)-1
        
        while i>=0:
            if s[i]=='#':
                answer = chr(int(s[i-2:i])+96) + answer
                i-=3
            else:
                answer = chr(int(s[i])+96) + answer
                i-=1
        
        return answer