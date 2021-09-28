# *을 n개 출력하되 w개마다 줄바꿈하기 1

n = int(input('몇 개를 출력할까요?'))
w = int(input('몇 개마다 줄바꿈할까요?'))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()

if n % w:
    print()

# 반복할때 마다 if문을 실행하므로 효율적이지 않다.
