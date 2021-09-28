# 오른쪽 아래가 직각인 이등변 삼각형으로 *출력하기

print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력해주세요'))

for i in range(n):
    # 공백을 출력하는 반복문
    for space in range(n - i - 1):
        print(' ', end='')
    # 별을 출력하는 반복문
    for star in range(i + 1):
        print('*', end='')
    print()
