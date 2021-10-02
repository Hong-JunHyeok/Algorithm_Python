# 이진 검색 알고리즘의 실행 과정

from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1

    print('   |', end='')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4 * len(a) + 2) * '-')

    while True:
        pc = (pl + pr) // 2

        print('   |', end='')
        if pl != pc:
            print((pl * 4 + 1) * ' ' + '<-' +
                  ((pc - pl) * 4) * ' ' + '+', end='')
        else:
            print((pc * 4 + 1) * ' ' + '<+', end='')

        if pc != pr:
            print(((pc - pr) * 4 - 2) * ' ' + '->')

        else:
            print('->')

        print(f'{pc:3}|', end='')
        for i in range((len(a))):
            print(f'{a[i] : 4}', end="")

        print('\n   |')


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
