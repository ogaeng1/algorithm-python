import re
p = re.compile('[CAMBRIDGE]')

text = input()
print(p.sub('', text))