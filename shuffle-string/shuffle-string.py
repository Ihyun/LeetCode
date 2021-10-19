class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sol = []
        for i, c in enumerate(s):
            sol.append((indices[i], c))
        sol.sort()
        answer = ""
        for c in sol:
            answer += c[1]
        return answer
        