import re
p = re.compile('[aeiouAEIOU]')

while True:
  text = input()

  if text == "#":
    break
  else:
    print(len(p.findall(text)))