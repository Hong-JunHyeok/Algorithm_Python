# 배열 원소를 역순으로 정렬하기
# O(n / 2)

a = [5, 4, 2, 2, 44, 1, 23, 3]
aLen = len(a)

for i in range(a // 2):
    a[i], [aLen - i - 1] = [aLen - i - 1], a[i]

print(a)
