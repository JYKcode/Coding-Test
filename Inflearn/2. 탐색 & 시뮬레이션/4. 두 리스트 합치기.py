# import sys
# sys.stdin=open("input.txt", "r")

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

p1=p2=0

sum_list = []

while p1<n and p2<m:
  if n_list[p1] < m_list[p2]:
    sum_list.append(n_list[p1])
    p1 += 1
  else:
    sum_list.append(m_list[p2])
    p2 += 1

if p1 < n:
  sum_list = sum_list + n_list[p1:]

if p2 < m:
  sum_list = sum_list + m_list[p2:]

print(sum_list)





  
      




