S = input()
sub_string = set()

for i in range(len(S)):
  for j in range(i+1, len(S)+1):
    sub_string.add(S[i:j])

print(len(sub_string))