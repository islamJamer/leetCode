class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if not s and not t: return True
        stack_s = []
        stack_t = []

        for i in s:
            if stack_s and i == '#':
                stack_s.pop()
            else:
                if i != '#':
                    stack_s.append(i)

        for i in t:
            if stack_t and i == '#':
                stack_t.pop()
            else:
                if i != '#':
                    stack_t.append(i)

        return stack_s == stack_t







if __name__ == '__main__':
    l = Solution()
    # s = "ab#c"
    # t = "ad#c"
    # s= "a##c"
    # t= "#a#c"
    # s= "y#fo##f"
    # t= "y#f#o##f"
    s= "a##c"
    t= "#a#c"
    print(l.backspaceCompare(s, t))