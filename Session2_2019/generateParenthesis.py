# Too slow recursive Solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A=[]):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append("(")
                generate(A)
                A.pop()
                A.append(")")
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for p in A:
                if p == "(":
                    bal +=1
                else:
                    bal -=1
                if bal < 0:
                    return False
            return bal == 0

        ans = []
        generate()
        return ans

# Backtrack is also slow
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S='', left=0, right=0):
            if len(S) == 2*n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)


        backtrack()
        return ans
