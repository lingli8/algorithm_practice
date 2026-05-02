class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res= []
        for t in tokens:
            if t == '+':
                res.append(res.pop() + res.pop())
            elif t == '-':
                second = res.pop()
                first = res.pop()
                res.append(first - second)
            elif t == '*':
                res.append(res.pop() * res.pop())
            elif t == '/':
                second = res.pop()
                first = res.pop()
                res.append(int(first/second))
            else:
                res.append(int(t))
        return res[0]