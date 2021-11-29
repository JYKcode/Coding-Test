def Count(len):
    cnt = 1
    sum_music = 0
    for x in music:
        if sum_music + x > len:
            cnt += 1
            sum_music = x
        else:
            sum_music += x
    return cnt

n, m = map(int, input().split())
music = list(map(int, input().split()))

maxx = max(music)
lt = 1
rt = sum(music)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if maxx <= mid and Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
