class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maximum = 0
        ln = len(nums)
        for i in range(ln//2):
            t = nums[i]+nums[ln-1-i]
            if maximum < t:
                maximum = t
        return maximum