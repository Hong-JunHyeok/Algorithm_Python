# 피보나치 수열 2
cache = {}
n = int(input())


def fibo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0

    if n in cache:
        return cache[n]
    result = fibo(n - 1) + fibo(n - 2)
    cache[n] = result
    return result


for i in range(2, n):
    fibo(i)

print(fibo(n))
