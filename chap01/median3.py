# 세 정수를 입력받아 중앙값 구하기 1

def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print(f"중앙값은 {med3(3,2,1)}입니다.")
print(f"중앙값은 {med3(3,4,8)}입니다.")
print(f"중앙값은 {med3(3,2,1)}입니다.")