class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backTrack(opend, closed):
            if opend == closed == n:
                res.append("".join(stack))
                return
            if opend < n:
                stack.append("(")
                backTrack(opend+1,closed)
                stack.pop()
            if opend > closed and closed < n:
                stack.append(")")
                backTrack(opend, closed+1)
                stack.pop()
        backTrack(0,0)
        return res