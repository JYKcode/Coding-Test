# import sys
# sys.stdin=open("input.txt", "r")

num_list = [i for i in range(21)]

for _ in range(10):
  a, b = map(int, input().split())
  for i in range((b-a+1)//2):
    num_list[a+i], num_list[b-i] = num_list[b-i], num_list[a+i]

num_list.pop(0)

for x in num_list:
  print(x, end=' ')



  
      




