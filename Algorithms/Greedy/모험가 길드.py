# 모험가 길드 

n = int(input())
data = sorted(list(map(int, input().split())))

result = 0
count = 0

for i in data:
  count += 1  # 첫 모험가를 포함 
  if count >= i: # i번째 공포도보다 모험가의 수가 크거나 같다면 (이상이라면) 
    result += 1 # 그룸을 구성함
    count = 0 # 모험가 수를 초기화함.

print(result)
