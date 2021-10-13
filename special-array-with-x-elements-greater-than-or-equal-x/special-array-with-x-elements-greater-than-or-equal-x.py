import bisect

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        lennums = len(nums)
        
        for i in range(lennums + 1):
            t = bisect.bisect_left(nums, i)
            if t == lennums - i:
                return i
            
        return -1
        