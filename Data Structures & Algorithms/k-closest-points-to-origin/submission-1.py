class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        x=[]

        for p in points:
            heapq.heappush(heap, (math.sqrt(p[0]**2 + p[1]**2), p))
        while k>0:
            x.append(heapq.heappop(heap)[1])
            k-=1
        return x
        
        
