class Solution(object):
    def longestValidParentheses(self, s):
        max_len = 0
        stack = [-1]  # Base boundary

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Unmatched ')' becomes the new base boundary
                    stack.append(i)
                else:
                    # Valid substring length = current index - top of stack
                    max_len = max(max_len, i - stack[-1])

        return max_len