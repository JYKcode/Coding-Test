# import sys
# sys.stdin=open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

lt = rt = (n // 2)

sum_apple = 0

for i in range(n):
  for j in range(lt, rt+1):
    sum_apple += a[i][j]
  if i < n//2:
    lt -= 1
    rt += 1
  else:
    lt += 1
    rt -= 1

print(sum_apple)








  
      




