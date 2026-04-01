class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        
        pair = sorted(pair)
        for i, j in pair[::-1]:
            time = (target - i)/j
            stack.append(time)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)
            