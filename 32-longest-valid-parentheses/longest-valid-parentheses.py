class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        mx_len=0
        for i,ch in enumerate(s):
            if ch=="(":stack.append(i)
            else:
                stack.pop()
                if not stack:stack.append(i)
                else:mx_len=max(mx_len,i-stack[-1])
        return mx_len


        