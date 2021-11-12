# import sys
# sys.stdin=open("input.txt", "rt")

from collections import deque

n, k = map(int, input().split())

ls = [i for i in range(1, n+1)]
ls = deque(ls)

while ls:
  for _ in range(k-1):
    cur = ls.popleft()
    ls.append(cur)
  ls.popleft()

  if len(ls) == 1:
    print(ls[0])
    ls.popleft()



  
      




