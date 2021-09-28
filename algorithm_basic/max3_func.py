def max3(a,b,c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum

print(f'max3(3, 1, 2) = {max3(3,1,2)}')
print(f'max3(1, 2, 3) = {max3(1,2,3)}')