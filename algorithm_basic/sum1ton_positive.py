# 1부터 n까지 정수의 합 구하기 (n값은 양수만 입력받음)

print('1부터 n까지 정수의 합을 구합니다.')

while True:
    n = int(input('n의 값을 입력해주세요: '))
    if n > 0:
        break

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
