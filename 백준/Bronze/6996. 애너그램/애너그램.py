T = int(input())

for _ in range(T):
  anagram = input().split()
  if sorted(anagram[0]) == sorted(anagram[1]):
    print(f"{anagram[0]} & {anagram[1]} are anagrams.")
  else:
    print(f"{anagram[0]} & {anagram[1]} are NOT anagrams.")