class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        stack2 = []
        for x in range(0, len(S)):
            if S[x] == "#":
                if len(stack1)!=0:
                    stack1.pop()
            else:
                stack1.append(S[x])
        for y in range(0, len(T)):
            if T[y] == "#":
                if len(stack2)!=0:
                    stack2.pop()
            else:
                stack2.append(T[y])
        return stack1==stack2
