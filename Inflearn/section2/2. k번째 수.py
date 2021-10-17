t = int(input())

for i in range(t):
  n, s, e, k = map(int, input().split())
  num_list = list(map(int, input().split()))
  num_list = num_list[s-1:e]
  num_list.sort()
  print(f'#{i+1} {num_list[k-1]}')



