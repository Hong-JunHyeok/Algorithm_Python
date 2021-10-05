# 단순 선택 정렬 알고리즘 구현하기

from typing import MutableSequence


def selection_sort(a: MutableSequence) -> None:
    n = len(a)

    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j

        a[i], a[min] = a[min], a[i]


if __name__ == '__main__':
    print('단순 선책 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    selection_sort(x)

    print('=' * 30)

    for i in range(num):
        print(f'x[{i}] = {x[i]}')
