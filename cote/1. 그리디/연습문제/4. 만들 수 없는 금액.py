n = int(input())
data = list(map(int, input().split()))
data.sort()

money = 1

for x in data:
    if money < x:
        break
    money += x

print(money)