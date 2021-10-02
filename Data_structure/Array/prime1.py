# 1000 이하의 소수를 나열하기
# 소수란? 2부터 n - 1까지 어떤 정수로도 나누어 떨어지지 않는 수

counter = 0

for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n % i == 0:
            break
    else:
        print(n)

print(f'나눗셈을 실행한 횟수 : {counter}')
