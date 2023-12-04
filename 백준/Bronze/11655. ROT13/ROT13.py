s = input()
res = ''

for i in s:
  if i == ' ' or i.isdigit():
    res += i
  elif i.isalpha():
    if i.isupper() and ord(i)+13 > 90:
      res += chr(ord(i) - 13)
    elif i.isupper() and ord(i)+13 <= 90:
      res += chr(ord(i) + 13)
    elif i.islower() and ord(i)+13 > 122:
      res += chr(ord(i) - 13)
    elif i.islower() and ord(i)+13 <= 122:
      res += chr(ord(i) + 13)

print(res)