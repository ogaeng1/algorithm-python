import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

str1_len = len(str1)
str2_len = len(str2)

dp = [[0] * (str2_len+1) for _ in range(str1_len + 1)]

for i in range(str1_len):
  for j in range(str2_len):
    if str1[i] == str2[j]:
      dp[i+1][j+1] = dp[i][j] + 1
    else:
      dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[str1_len][str2_len])
res = []

while str1_len > 0 and str2_len > 0:
  if str1[str1_len-1] == str2[str2_len-1]:
    res.append(str1[str1_len-1])
    str1_len -= 1
    str2_len -= 1
  elif dp[str1_len-1][str2_len] > dp[str1_len][str2_len-1]:
    str1_len -= 1
  else:
    str2_len -= 1

print(''.join(reversed(res)))