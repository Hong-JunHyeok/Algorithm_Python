def recursive_power(base, power):
    """
    거듭제곱을 "재귀적"으로 계산해주세요.
    :param base: 거듭 제곱의 밑
    :param power: 거듭 제곱의 지수
    :return: base ^ power 의 값, 예) 2³ = 8
    """

    if power == 0:
        return 1
    if power == 1:
        return base
    return base * recursive_power(base, power - 1)


def non_recursive_power(base, power):
    """
    재귀를 사용하지 않고 거듭제곱을 계산해주세요.
    :param base: 거듭 제곱의 밑
    :param power: 거듭 제곱의 지수
    :return: base ^ power 의 값, 예) 2³ = 8
    """
    total = 1
    for _ in range(power):
        total *= base

    return base ** power


if __name__ == '__main__':
    # ==================== 코드 수정 불필요 ==================== #
    # 이 셀은 위에 작성한 셀의 테스트 용입니다.
    # 필요시 수정해도 되지만, 그대로 사용해도 됩니다.

    base = 3
    power1 = 3
    power2 = 4
    print(f"Recursive {base}^{power1}: {recursive_power(base, power1)}")
    print(
        f"Non-Recursive {base}^{power1}: {non_recursive_power(base, power1)}")
    print(f"Recursive {base}^{power2}: {recursive_power(base, power2)}")
    print(
        f"Non-recursive {base}^{power2}: {non_recursive_power(base, power2)}")

    power1 = 0
    print(f"Recursive {base}^{power1}: {recursive_power(base, power1)}")
    print(
        f"Non-recursive {base}^{power1}: {non_recursive_power(base, power1)}")
    # ==================== 코드 수정 불필요 ==================== #
