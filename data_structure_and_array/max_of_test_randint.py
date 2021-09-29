# 배열 원소의 최대값을 구해서 출력하기 (원소값을 난수로 생성)

import random
from max import max_of

print('난수의 최대값을 구합니다.')
num = int(input('난수의 개수를 입력하세요 : '))
lo = int(input('난수의 최소값를 입력하세요 : '))
hi = int(input('난수의 최대값를 입력하세요 : '))
x = [None] * num

for i in range(num):
    x[i] = random.randint(lo, hi)  # lo이상 hi이하의 정수 난수를 반환

print(f'{(x)}')
print(f'이 가운데 최대값은 {max_of(x)}입니다.')
