# 세 정수를 입력받아 중앙값 구하기 2

def med3(a,b,c):
    if(b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c
# 이미 비교를 마친 상태에서 다시 비교를 하는 알고리즘이므로 효율적인 방법은 아님

print(f"중앙값은 {med3(3,2,1)}입니다.")
print(f"중앙값은 {med3(3,4,8)}입니다.")
print(f"중앙값은 {med3(3,2,1)}입니다.")