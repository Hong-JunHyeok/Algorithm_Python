# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 입력된 데이터에 대해 정렬하고 출력하시오

# arr = [5, 4, 8, 3]
# arr.sort()

# for i in arr:
#     print(i, end=' ')

# 입력

# [입력]
# 5
# 4 8 2 5 9

# [출력]
# 2 4 5 8 9

n = int(input())
arr = list(map(int, input().split(' ')))  # 배열로 쉽게 만들어줌

print(*sorted(arr))

# for i in range(count):
#     arr.append(int(input()))

# arr.sort()

# for i in arr:
#     print(i, end=' ')


# 정렬 프로그램을 작성하시오.
# [입력]
# 5
# 2 4
# 4 8 2 5 9

# [출력]
# 2 5 8
# n = int(input())
# m1, m2 = map(int, input().split())
# li = list(map(int, input().split()))
