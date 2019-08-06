class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        br_dict = {')': '(', ']': '[', '}': '{'}
        stack = []
        for br in s:
            if br in br_dict:
                openbr = stack.pop() if stack else '$'
                if openbr != br_dict[br]:
                    return False
            else:
                stack.append(br)

        return not stack
