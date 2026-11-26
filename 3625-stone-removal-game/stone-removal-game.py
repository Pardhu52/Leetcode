class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones=10
        ali=True
        while n>=stones:
            n-=stones
            stones-=1
            ali=not ali
        return not ali
        