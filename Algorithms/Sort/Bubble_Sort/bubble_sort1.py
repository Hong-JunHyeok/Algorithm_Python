# 버블 정렬 알고리즘 구현하기

from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬"""
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, - 1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]


if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    bubble_sort(x)

    print('=' * 30)

    for i in range(num):
        print(f'x[{i}] = {x[i]}')
