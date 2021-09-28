# +와 -를 번갈아가면서 출력하기

n = int(input('몇 개를 출력할까요?'))

for i in range(n):
    if i % 2:
        print('-',end='')
    else:
        print('+',end='')

print()