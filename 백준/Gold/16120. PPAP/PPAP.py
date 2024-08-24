import sys
input = sys.stdin.readline

ppapString = input().strip()
stack = []

for c in ppapString:
    stack.append(c)
    if len(stack) >= 4 and ''.join(stack[-4:]) == "PPAP":
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append('P')

ppap = "".join(stack)
print("PPAP" if ppap == "P" else "NP")
