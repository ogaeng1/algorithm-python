from collections import Counter

english_name = list(map(str, input()))
english_name.sort()
palindrome = Counter(english_name)

odd_cnt = 0
center_str = ''
res = ''

for i in palindrome:
  if palindrome[i] % 2 != 0:
    odd_cnt += 1
    center_str += i

  for _ in range(palindrome[i] // 2):
    res += i

if odd_cnt > 1:
  print("I'm Sorry Hansoo")
elif odd_cnt == 0:
  print(res + res[::-1])
else:
  print(res + center_str + res[::-1])