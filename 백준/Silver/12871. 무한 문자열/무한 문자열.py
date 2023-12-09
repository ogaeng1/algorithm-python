s = input()
t = input()

len_s, len_t = len(s), len(t)

print(1 if s*len_t == t*len_s else 0)