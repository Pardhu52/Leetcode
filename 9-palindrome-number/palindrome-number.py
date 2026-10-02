class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:return False
        str_in=str(x)
        l=0
        rev=len(str_in)-1
        while l<rev:
            if str_in[l]!=str_in[rev]:
                return False
            l+=1
            rev-=1
        return True

        