import sys
from operator import itemgetter
# sys.stdin=open("input.txt", "r")

n = int(input())
time = []

for i in range(n):
  s, e = map(int, input().split())
  time.append((s, e))

time.sort(key=itemgetter(1))

res = 0
end_time = 0
for x in time:
  if end_time <= x[0]:
    res += 1
    end_time = x[1]
  else:
    continue

print(res)








  
      




