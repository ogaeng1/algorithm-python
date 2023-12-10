import sys
s = sys.stdin.readline()

change_0, change_1 = 0, 0

if s[0] == '0':
  change_1 += 1
else:
  change_0 += 1

for i in range(len(s) - 1):
  if s[i] != s[i+1]:
    if s[i] == '0':
      change_1 += 1
    else:
      change_0 += 1

print(min(change_0, change_1))