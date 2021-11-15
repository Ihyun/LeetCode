class Solution:
    def fib(self, n: int) -> int:
        sol = [0, 1]
        
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            for i in range(n-1):
                sol.append(sol[-1]+sol[-2])
            
            return sol[-1]