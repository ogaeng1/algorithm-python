doc = input()
word = input()

while word in doc:
  doc = doc.replace(word, '*', 1)

print(doc.count('*'))