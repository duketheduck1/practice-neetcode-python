class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = []
        for i in range( len(position)):
            pair.append([position[i], speed[i]])
        
        pair = sorted(pair)
        for i, s in pair[::-1]:
            time = (target - i)/s
            stack.append(time)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)