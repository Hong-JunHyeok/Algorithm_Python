# 입력받은 정수의 부호를 출력하기

n = int(input('정수를 입력하세요: '))

if n > 0:
    print('이 수는 양수입니다.')
elif n < 0:
    print('이 수는 음수입니다')
else:
    print('이 수는 0입니다.')