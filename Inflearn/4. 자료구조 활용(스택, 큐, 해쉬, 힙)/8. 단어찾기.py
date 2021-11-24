# Method Mine
n = int(input())

word_list = []
use = []

for i in range(n + (n - 1)):
  word = input()
  if i < n:
    word_list.append(word)
  else:
    use.append(word)

for x in use:
  word_list.remove(x)

print(word_list[0])

# Method Lecture
n = int(input())
p = dict()

for i in range(n):
    word = input()
    p[word] = 1

for i in range(n-1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)