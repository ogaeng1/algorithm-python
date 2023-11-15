import re

text = input()
p = re.compile('[aeiou]')

print(len(p.findall(text)))