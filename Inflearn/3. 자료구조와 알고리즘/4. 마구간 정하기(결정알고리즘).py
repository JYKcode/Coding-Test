def Count(len):
    cnt = 1
    ep = gap[0]
    for i in range(1, n):
        if gap[i] - ep >= len:
            cnt += 1
            ep = gap[i]
    return cnt

n, c = map(int, input().split())
gap = []

for i in range(n):
    tmp = int(input())
    gap.append(tmp)

gap.sort()

lt = 1
rt = max(gap)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)