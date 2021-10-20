# Method Mine
n = int(input())

cnt = [0] * (n+3)

for i in range(2, n+1):
  cnt[i] += 1
  for j in range(i, n+1, i):
    cnt[j] += 1

cnt_num = 0

for i in cnt:
  if i == 2:
    cnt_num += 1

print(cnt_num)

# Method Lecture
n = int(input())
ch = [0] * (n+1)
cnt = 0

for i in range(2, n+1):
  if ch[i] == 0:
    cnt += 1
  for j in range(i, n+1, i):
    ch[j] = 1

print(cnt)