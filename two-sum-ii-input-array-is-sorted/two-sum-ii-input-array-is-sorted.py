class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lennum = len(numbers)
        for i in range(lennum):
            lo = i+1
            hi = lennum
            t = target-numbers[i]
            while lo<hi:
                mid = (lo+hi)//2
                if numbers[mid]<t:
                    lo = mid + 1
                else:
                    hi = mid
            
            if lo<lennum and numbers[lo]==t:
                return [i+1, lo+1]
            
        