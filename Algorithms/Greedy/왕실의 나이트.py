# 왕실의 나이트 

input_data = input()
# 현 나이트의 위치를 파악
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 모든 경우의 수를 정의
steps = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

result = 0
for step in steps:
  # 각 스탭별로 이동한 후에 
  next_row = row + step[0]
  next_column = column + step[1]
  # 해당 스탭이 유효한 범위인지 확인
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)
