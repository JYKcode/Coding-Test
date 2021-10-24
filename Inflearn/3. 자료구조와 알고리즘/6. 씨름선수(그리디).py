import sys
# sys.stdin=open("input.txt", "r")

n = int(input())
body = []

for _ in range(n):
  t, w = map(int, input().split())
  body.append((t, w))

body.sort(reverse=True)

cnt = 0
weight = 0
for x in body:
  if weight < x[1]:
    weight = x[1]
    cnt += 1

print(cnt)










  
      




