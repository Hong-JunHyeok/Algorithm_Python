# 유클리드 호제법으로 최대 공약수 구하기

def gcd(x: int, y: int) -> int:
    print(x, y)
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


if __name__ == '__main__':
    x = int(input('첫 번째 정숫값을 입력하세요.'))
    y = int(input('두 번째 정숫값을 입력하세요.'))

    print(f'GCD : {gcd(x,y)}')
