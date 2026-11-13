class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x=len(nums)+1
        res1=[1]*x
        res2=[1]*x
        res=[1]*(x-1)

        for i in range(1,x-1):
            res1[i]=nums[i-1]*res1[i-1]
            res2[x-i-1]=res2[x-i]*nums[x-i-1]
        res1=res1[:x-1]
        res2=res2[1:]

        for i in range(x-1):
            res[i]=res1[i]*res2[i]
        return res
        
