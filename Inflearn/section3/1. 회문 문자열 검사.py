# import sys
# sys.stdin=open("input.txt", "r")

n = int(input())

for i in range(1, n+1):
  str = input()
  str = str.upper()
  for j in range(len(str)//2):
    if str[j] != str[-1-j]:
      print(f"#{i} NO")
      break
  else:
    print(f"#{i} YES")
  


  
      




