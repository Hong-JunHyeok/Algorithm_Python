# 이진 검색 알고리즘 2

from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    pl = 0  # 배열의 첫번째 인덱스
    pr = len(a) - 1  # 배열의 마지막 인덱스

    while True:
        pc = (pl + pr) // 2  # 중앙 값을 구하는 식
        if a[pc] == key:  # 탐색이 성공한 경우
            return pc
        elif a[pc] < key:  # key값이 a[pc]보다 큰 경우
            pl = pc + 1  # 검색 범위를 뒤쪽 절반으로 좁힘
        else:  # key값이 a[pc]보다 작은 경우
            pr = pc - 1

        if pl > pr:  # 검색 실패
            break


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요'))
    x = [None] * num

    print('배열 데이터를 오름차순으로 입력하세요 : ')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= x[i - 1]:
                break

    ky = int(input('검색할 값을 입력하세요 : '))

    idx = bin_search(x, ky)

    if idx == -1:
        print('없습니다.')
    else:
        print(f'x[{idx}]')
