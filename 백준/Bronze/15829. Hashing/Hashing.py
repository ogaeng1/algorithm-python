l = int(input())
word = input()

m = 1234567891
hash = 0

for i in range(l):
  hash = (hash + (ord(word[i]) - ord('a')+1) * (31**i)) % m

print(hash)