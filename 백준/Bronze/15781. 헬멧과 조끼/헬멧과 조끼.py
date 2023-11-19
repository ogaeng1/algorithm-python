N, M = map(int, input().split())
helmet = list(map(int, input().split()))
armor = list(map(int, input().split()))

print(max(helmet) + max(armor))