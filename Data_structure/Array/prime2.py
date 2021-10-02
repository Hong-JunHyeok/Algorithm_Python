# 1000 이하의 소수를 나열하기
# 소수란? 2부터 n - 1까지 어떤 정수로도 나누어 떨어지지 않는 수
# 알고리즘 개선 버전

counter = 0  # 나눗셈 횟수를 카운트
ptr = 0  # 이미 찾은 소수의 개수
prime = [None] * 500  # 소수를 저장하는 배열

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2):  # 홀수만을 대상으로 설정
    for i in range(1, ptr):
        counter += 1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])

print(f'나눗셈을 실행한 횟수 : {counter}')
