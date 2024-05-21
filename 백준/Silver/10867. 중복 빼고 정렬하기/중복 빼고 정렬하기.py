import sys
input = sys.stdin.readline

N = int(input().strip())
num = sorted(set(map(int, input().split())))

print(*num)