# 문자열 재정렬

s = input()

chars = sorted([c for c in s if 65 <= int(ord(c)) <= 90], key= lambda x : x)
nums = [int(c) for c in s if 48 <= int(ord(c)) <= 57]

print(''.join(chars) + str(sum(nums)))
