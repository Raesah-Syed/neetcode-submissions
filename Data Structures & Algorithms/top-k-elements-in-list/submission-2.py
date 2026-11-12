class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        res=[]

        for n in nums:
            d[n]=d.get(n,0)+1

        sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)

        res = [item[0] for item in sorted_items[:k]]
        return res
        
