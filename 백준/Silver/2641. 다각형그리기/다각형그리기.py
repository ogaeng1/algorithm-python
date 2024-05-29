n = int(input())
base = list(map(int, input().split()))
m = int(input())
m_list = [list(map(int, input().split())) for _ in range(m)]

result = []
for i in m_list:
    r_mlist = list(map(lambda x: {1: 3, 2: 4, 3: 1, 4: 2}[x], i))[::-1]
    if base == i or base == r_mlist:
        result.append(i)
        continue

    for j in range(1, len(base)):
        tmp = i[j:] + i[:j]
        r_tmp = r_mlist[j:] + r_mlist[:j]
        if base == tmp or base == r_tmp:
            result.append(i)
            break

print(len(result))
for res in result:
    print(*res)