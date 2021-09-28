# 1부터 n까지 정수의 합 구하기 1(while문)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n의 값을 입력하세요: '))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')