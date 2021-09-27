class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        
        for timePoint in timePoints:
            hour, minute = map(int, timePoint.split(":"))
            times.append(hour*60+minute)
        
        times.sort()
        minimum = 1440//2
        
        for i in range(len(times)-1):
            if times[i+1]-times[i]<minimum:
                minimum = times[i+1]-times[i]
        
        if times[0]+(1440-times[-1])<minimum:
            minimum = times[0]+(1440-times[-1])
        
        return minimum
            
        