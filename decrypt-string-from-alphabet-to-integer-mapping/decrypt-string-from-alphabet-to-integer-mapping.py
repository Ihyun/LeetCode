class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = ''
        anslist = []
        
        i = len(s)-1
        
        while i>=0:
            if s[i]=='#':
                anslist.append(int(s[i-2:i]))
                i-=3
            else:
                anslist.append(int(s[i]))
                i-=1
                
        anslist.reverse()
        
        for num in anslist:
            answer += chr(num+96)
        
        return answer
        