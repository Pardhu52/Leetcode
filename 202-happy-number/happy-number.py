class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        dup=set()
        while(n!=1):
            sum=0
            if n in dup:
                return False
            dup.add(n)
            while(n>0):
                rem=n%10
                sum+=rem*rem
                n//=10
            n=sum
        return True