class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        has = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i not in has:
                stack.append(i)
            if i in has :
                if stack and has[i] == stack[-1]:
                    stack.pop()
                else: 
                    return False
        return stack == []