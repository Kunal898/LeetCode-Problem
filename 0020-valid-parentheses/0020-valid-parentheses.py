class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        brackets = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for x in s:
            if x in brackets:
                if not stack or stack.pop() != brackets[x]:
                    return False
            else:
                stack.append(x)

        return len(stack) == 0