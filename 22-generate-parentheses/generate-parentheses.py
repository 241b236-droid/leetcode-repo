class Solution(object):
    def generateParenthesis(self, n):

        result = []
        self._backtrack(result, [], 0, 0, n)
        return result

    def _backtrack(self, result, current, open_count, close_count, n):
        # Base case: string is complete
        if len(current) == 2 * n:
            result.append("".join(current))
            return
        # Place '(' if we haven't used all n opening brackets
        if open_count < n:
            current.append('(')
            self._backtrack(result, current, open_count + 1, close_count, n)
            current.pop()
        # Place ')' only if it won't create an invalid prefix
        if close_count < open_count:
            current.append(')')
            self._backtrack(result, current, open_count, close_count + 1, n)
            current.pop()