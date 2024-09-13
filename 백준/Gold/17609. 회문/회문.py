import sys
input = sys.stdin.readline

def palindrome(word):
  left, right = 0, len(word)-1
  
  if word == word[::-1]:
    return 0

  while left < right:
    if word[left] != word[right]:
      temp1 = word[left+1:right+1]
      temp2 = word[left:right]
      if temp1 == temp1[::-1] or temp2 == temp2[::-1]:
        return 1
      else:
        return 2

    left += 1
    right -= 1

T = int(input())

for i in range(T):
  word = input().rstrip()
  print(palindrome(word))