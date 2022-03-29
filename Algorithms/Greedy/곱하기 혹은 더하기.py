# 곱하기 혹은 더하기

def cmp(a, b):
  if a + b > a * b:
    return a + b
  else:
    return a * b
    
n = list(map(int, input()))
result = cmp(n[0], n[1])

for index in range(1, len(n) - 1):
  result = cmp(result, n[index + 1])

print(result)
