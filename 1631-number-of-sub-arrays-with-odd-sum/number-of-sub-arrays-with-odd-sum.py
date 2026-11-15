
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod=10**9+7
        even=1
        odd=0
        res=0
        parity=0
        for num in arr:
            parity^=(num%2)
            if parity==1:
                res+=even
                odd+=1
            else:
                res+=odd
                even+=1
            res%=mod
        return res
