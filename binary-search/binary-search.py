class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo<hi:
            mid = (lo + hi) // 2
            if nums[mid]<target:
                lo = mid + 1
            else:
                hi = mid
        if lo<0 or lo>=len(nums):
            return -1
        elif nums[lo]==target:
            return lo
    
        return -1
        
        