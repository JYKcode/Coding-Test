# Method Mine
def DFS(x):
    if x > 0:
        a.insert(0, x % 2)
        x = x // 2
        DFS(x)

n = int(input())
a = []

DFS(n)

for x in a:
    print(x, end='')

# Method Lecture
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x % 2, end='')

n = int(input())
DFS(n)