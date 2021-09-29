# +와 -를 번갈아가면서 출력하기2

n = int(input('몇 개를 출력할까요?'))

for _ in range(n // 2):
    print('+-', end='')

if n % 2:
    print('+', end='')

print()
