# Method Lecture
def reverse(x):
  reversed_num = 0
  while x > 0:
    t = x % 10
    reversed_num = reversed_num*10 + t
    x //= 10
  return reversed_num

def isPrime(x):
  if x == 1:
    return False
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

n = int(input())
a = list(map(int, input().split()))

for x in a:
  reversed_num = reverse(x)
  isprime = isPrime(reversed_num)
  if isprime == True:
    print(reversed_num, end=' ')