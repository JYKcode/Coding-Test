# import sys
# sys.stdin=open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))

cnt = [0] * n

for i in range(n):
  for j in range(n):
    if(a[i] == 0 and cnt[j] == 0):
      cnt[j] = i + 1
      break

    elif cnt[j] == 0:
      a[i] -= 1

for x in cnt:
  print(x, end=' ')







  
      




