import sys
input = sys.stdin.readline
n, m = map(int, input().split())

not_listen = [input() for i in range(n)]
not_see = [input() for i in range(m)]
human = []

result = list(set(not_listen) & set(not_see))
result.sort()

print(len(result))
print(''.join(result), end='')