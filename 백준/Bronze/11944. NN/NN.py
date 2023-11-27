N, M = map(int, input().split())
result = str(N) * N

print(result if len(result) <= M else result[:M])