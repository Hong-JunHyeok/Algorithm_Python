def hanoi(disk_num: int, x: int, y: int) -> None:
    if disk_num > 1:
        hanoi(disk_num - 1, x, 6 - x - y)

    print(f'[{x}]에 있는 원판{x}를 {y}로 옮깁니다.')

    if disk_num > 1:
        hanoi(disk_num - 1, 6 - x - y, y)


hanoi(3, 1, 3)
