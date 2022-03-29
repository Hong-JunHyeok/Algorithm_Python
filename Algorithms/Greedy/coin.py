# 매 순간 가장 좋은 결과만을 고르는 방식

# 문제 풀이를 위한 최소한의 아이디어를 떠올리고 그것이 정당한지 검토하는 작업이 중요함.
n = 1260
count = 0

array = [500, 100 , 50 ,10]

for coin in array:
  count += n // coin # 2 + 2 + 1 + 1
  n %= coin # 260 60 10 0

print(count)
