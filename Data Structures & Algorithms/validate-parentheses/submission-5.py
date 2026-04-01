class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        dic = {"}":"{", "]":"[", ")":"("}
        for i in s:
            if i not in dic:
                stack.append(i)
            elif i in dic and len(stack):
                if dic[i] == stack.pop():
                    continue
                else:
                    return False
            else:
                return False
        return len(stack) == 0