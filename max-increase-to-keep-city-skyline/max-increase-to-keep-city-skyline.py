class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        sol = 0
        transposed = []
        
        for j in range(len(grid)):
            temp = []
            for i in range(len(grid)):
                temp.append(grid[i][j])
            transposed.append(temp)
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sol += min(max(grid[i]), max(transposed[j])) - grid[i][j]
                
        return sol
        