class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        res=float('inf')
        for leng in range(l,r+1):
            curr_sum=sum(nums[:leng])
            if curr_sum>0:
                res=min(res,curr_sum)
            for i in range(leng,n):
                curr_sum+=nums[i]-nums[i-leng]
                if curr_sum>0:
                    res=min(res,curr_sum)
        return res if res!=float('inf') else -1