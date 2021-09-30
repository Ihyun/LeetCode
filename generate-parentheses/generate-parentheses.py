class Solution:
    
    global sol
    
    def dfs(self, lefts: int, subsum: int, subsol: str):
        global sol
        if subsum<0:
            return
        elif subsum==0 and lefts==0:
            sol.append(subsol)
            return
                
        if lefts>0:
            self.dfs(lefts-1, subsum+1, subsol+'(')
        self.dfs(lefts, subsum-1, subsol+')')
        
        return
        
        
    
    def generateParenthesis(self, n: int) -> List[str]:
        global sol
        sol = []
        self.dfs(n, 0, '')
        return sol