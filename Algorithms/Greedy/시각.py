# 시각 3이 들어가는 경우의 수 구하기
count = 0

for h in range(24):
  for m in range(60):
    for s in range(60):
      if '3' in str(h) + str(m) + str(s):
        count += 1

print(count)
