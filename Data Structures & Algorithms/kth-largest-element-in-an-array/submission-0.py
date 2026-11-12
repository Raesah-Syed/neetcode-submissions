class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]

        r=[-x for x in nums]

        heapq.heapify(r)

        while k-1>0:
            heapq.heappop(r)
            k-=1
        
        return -(heapq.heappop(r))
