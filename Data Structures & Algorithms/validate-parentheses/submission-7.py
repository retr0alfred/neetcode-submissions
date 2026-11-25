class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if (stack != []) and ((i == ")" and stack[-1] == '(') or (i == "]" and stack[-1] == '[') or (i == "}" and stack[-1] == '{')):
                stack.pop()
            elif i in "({[":
                stack.append(i)
            else:
                return False
        print(stack)
        
        return stack == []