class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        dic = {"}":"{", "]":"[", ")":"("}
        for i in s:
            if i in dic and len(stack):
                if dic[i] == stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0