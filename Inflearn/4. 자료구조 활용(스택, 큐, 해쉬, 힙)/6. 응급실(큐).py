import sys
from collections import deque
# sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())
p = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
p = deque(p)
cnt = 0
while True:
  cur = p.popleft()
  if any(cur[1] < x[1] for x in p):
    p.append(cur)
  else:
    cnt += 1
    if cur[0] == m:
      print(cnt)
      break
  






  
      




