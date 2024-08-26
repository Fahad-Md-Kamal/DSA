class Solution:
    def isValid(self, s: str) -> bool:
        tmp_stack = []
        parentheses = {")": "(" , "}":"{", "]": "["}
        for c in s:
            if c in ["(", "{", "["]:
                tmp_stack.append(c)
            elif tmp_stack:
                if parentheses[c] != tmp_stack.pop():
                    return False
            else:
                return False
        return len(tmp_stack) == 0
    

if __name__ == "__main__":
    res = Solution().isValid(']')
    print(res)
