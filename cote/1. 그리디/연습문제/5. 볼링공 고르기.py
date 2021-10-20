n, m = map(int, input().split())
weight = list(map(int, input().split()))

weight.sort()

cnt = 0
for i in range(n):
    for j in range(i, n):
        if weight[i] != weight[j]:
            cnt += 1

print(cnt)