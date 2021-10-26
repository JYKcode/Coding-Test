# import sys
# sys.stdin=open("input.txt", "r")

from collections import deque
n, m = map(int, input().split())
weight_list = list(map(int, input().split()))
weight_list.sort()
weight_list = deque(weight_list)

cnt = 0

while weight_list:
  if len(weight_list) == 1:
    cnt += 1
    break

  if weight_list[0] + weight_list[-1] > m:
    weight_list.pop()
    cnt += 1
  
  else:
    weight_list.popleft()
    weight_list.pop()
    cnt += 1

print(cnt)







  
      




