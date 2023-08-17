class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def typeString(st: str) -> List[str]:
            stack = []

            for ch in st: 
                if ch == '#': 
                    if stack: 
                        stack.pop()
                else: 
                    stack.append(ch)

            return stack

        if typeString(s) == typeString(t):
            return True

        return False