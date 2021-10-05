def solution(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    ptr = 0
    prime = [None] * n

    prime[ptr] = 2
    ptr += 1

    prime[ptr] = 3
    ptr += 1

    for num in range(5, n + 1, 2):
        i = 1
        while prime[i] * prime[i] <= num:
            if num % prime[i] == 0:
                break
            i += 1
        else:
            prime[ptr] = num
            ptr += 1
    return ptr


if __name__ == '__main__':
    solution(0)
