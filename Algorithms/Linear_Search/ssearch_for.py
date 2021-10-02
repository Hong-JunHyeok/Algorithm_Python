from typing import Any, Sequence


def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i

    return -1


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요 : '))  # num 값을 입력받음
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요: '))

    idx = seq_search(x, ky)

    if idx == -1:
        print(f'검색값을 갖는 원소가 없습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
