class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        r=[-x for x in stones]
        heapq.heapify(r)
        while len(r)>1:
            x=-(heapq.heappop(r))
            y=-(heapq.heappop(r))
            if x>y:
                heapq.heappush(r,y-x)
            elif y>x:
                heapq.heappush(r,x-y)
            elif x==y:
                continue
        
        return -(heapq.heappop(r)) if len(r)!=0 else 0