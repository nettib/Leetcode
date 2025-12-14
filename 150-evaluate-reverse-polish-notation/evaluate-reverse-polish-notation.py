class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops_match = {
                        '+': lambda a, b: a + b, 
                        '-': lambda a, b: a - b, 
                        '*': lambda a, b: a * b, 
                        '/': lambda a, b: a / b
                    }
        nums = []

        for i in range(len(tokens)):
            if tokens[i] in ops_match:
                val2 = int(nums.pop())
                val1 = int(nums.pop())
                nums.append(ops_match[tokens[i]](val1, val2))
            else:
                nums.append(tokens[i])
        
        return int(nums[-1])
