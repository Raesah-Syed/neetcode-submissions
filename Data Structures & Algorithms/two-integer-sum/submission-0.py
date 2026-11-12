class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        res=[]
        for n in range(len(nums)):
            c=target-nums[n]
            if c in d:
                res=[d[c],n]
            d[nums[n]]=n
        return res
