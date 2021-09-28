class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        answer = []
        lens = []
        
        for word in words:
            lens.append(len(word))
        
        maxlen = max(lens)
        
        for i in range(maxlen):
            temp = ""
            for j in range(len(words)):
                if i < lens[j]:
                    temp += words[j][i]
                else:
                    temp += ' '
            
            answer.append(temp.rstrip())
        
        return answer
            
                    