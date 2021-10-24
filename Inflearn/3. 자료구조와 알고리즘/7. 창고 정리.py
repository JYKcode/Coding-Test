import sys
# sys.stdin=open("input.txt", "r")

row = int(input())
box_height = list(map(int, input().split()))
m = int(input())

box_height.sort()

for _ in range(m):
  box_height[0] += 1
  box_height[row - 1] -= 1
  box_height.sort()

print(box_height[row - 1] - box_height[0])









  
      




