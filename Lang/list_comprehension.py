n,m = 3, 4

# 리스트 컴프리핸션의 좋은 예
map = [[0] * n for _ in range(m)]
map[1][1] = 5
print(map)

# 리스트 컴프리헨션의 나쁜 예
map = [[0] * n] * m # 리스트의 객체 값을 참조하는 2차원 리스트를 생성해버리기 때문에 이런 문제가 발생한다.
map[1][1] = 5
print(map) 


# 파이썬에서 특정 값을 가지는 모는 원소를 지우는 컴프리헨션
a = [1,2,3,4,5,6,6,5,5,5,6]
remove_set = {5, 6}

# remove_set에 포함되지 않는 원소만 남겨두는 작업을 수행함.
result = [i for i in a if i not in remove_set]
print(result)
