import time


def is_sorted(array):
    """
    배열이 오름차순으로 정렬되어 있는지 확인하세요. (array의 요소는 int/float 숫자형입니다.)
    :param array: 확인해야 하는 배열
    :return: Boolean (True / False)
    """
    flag = 0
    for i in range(len(array)):
        if flag <= array[i]:
            flag = array[i]
        else:
            return False
    return True


def binary_search(array, elem, first, last):
    """
    이진 검색을 활용하여 배열 내 요소를 찾아보세요.
    :param array: 요소를 찾아야하는 배열
    :param elem: 찾으려는 요소
    :param first: 배열의 첫번째 인덱스
    :param last: 배열의 마지막 인덱스
    :return: Boolean (True / False)
    """
    middle = (first + last) // 2
    if array[middle] == elem:
        return True

    if first == last:
        return False

    if elem > array[middle]:
        return binary_search(array, elem, middle + 1, last)
    elif elem < array[middle]:
        return binary_search(array, elem, first, middle - 1)

# ==================== 코드 수정 불필요 ==================== #
# 이 셀은 위에 작성한 셀의 테스트 용입니다.
# 필요시 수정해도 되지만, 그대로 사용해도 됩니다.


# A is sorted
A = (1, 5, 6, 7, 9, 13, 16, 17)
# B is not sorted
B = (1, 6, 7, 8, 2)


print(f'A 정렬 여부: {is_sorted(A)}')
print(f'B 정렬 여부: {is_sorted(B)}')

# time.sleep(2)

# A에서 16 찾기
result = binary_search(A, 16, 0, len(A) - 1)
print(f'A에서 16 찾기: {result}')

# time.sleep(2)

# A에서 56 찾기
result = binary_search(A, 56, 0, len(A) - 1)
print(f'A에서 56 찾기: {result}')
# ==================== 코드 수정 불필요 ==================== #
