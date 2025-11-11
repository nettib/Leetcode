class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        p1 = p2 = 0

        while p1 < len(pushed) or p2 < len(popped):
            if p1 < len(pushed):
                stack.append(pushed[p1])
                while stack and popped[p2] == stack[-1]:
                    stack.pop()
                    p2 += 1
                p1 += 1
            if p1 == len(pushed) and stack and popped[p2] != stack[-1]:
                return False
        
        return True