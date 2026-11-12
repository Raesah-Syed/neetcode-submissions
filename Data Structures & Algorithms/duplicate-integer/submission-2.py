class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=Counter(nums)
        res = any(v > 1 for k, v in c.items())
        return res
