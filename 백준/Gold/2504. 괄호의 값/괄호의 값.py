import sys
input = sys.stdin.readline

s = list(input().rstrip())
stack = []
acc = 1
res = 0

for i in range(len(s)):
    if s[i] == '(':
        acc *= 2
        stack.append(s[i])
    elif s[i] == '[':
        acc *= 3
        stack.append(s[i])
    elif s[i] == ')':
        if not stack or stack[-1] != '(':
            res = 0
            break
        if s[i-1] == '(':
            res += acc
        acc //= 2
        stack.pop()
    elif s[i] == ']':
        if not stack or stack[-1] != '[':
            res = 0
            break
        if s[i-1] == '[':
            res += acc
        acc //= 3
        stack.pop()
        
print(0 if stack else res)