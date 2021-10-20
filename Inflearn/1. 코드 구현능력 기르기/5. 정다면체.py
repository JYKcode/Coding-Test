import sys
# sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())

cnt = [0] * (n+m+1)

for i in range(1, n+1):
  for j in range(1, m+1):
    cnt[i+j] += 1

max_cnt = max(cnt)

for idx, x in enumerate(cnt):
  if x == max_cnt:
    print(idx, end=' ')
      




