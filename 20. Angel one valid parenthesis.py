class Solution:
    def isValid(self, s: str) -> bool:
        hasmap = {'}': '{', ']': '[', ')': '('}
        stack = []

        for i in s:
            if i not in hasmap:  # If it's an opening bracket
                stack.append(i)
            else:  # If it's a closing bracket
                if not stack:
                    return False
                popped = stack.pop()
                if popped != hasmap[i]:
                    return False

        return not stack  # Return True if the stack is empty, False otherwise
