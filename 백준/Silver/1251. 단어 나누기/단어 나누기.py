import sys
input = sys.stdin.readline

word = input().strip()
res = []

for i in range(1, len(word)):
  for j in range(i+1, len(word)):
    start = word[:i][::-1]
    mid = word[i:j][::-1]
    end = word[j:][::-1]

    res.append(start+mid+end)

res.sort()
print(res[0])