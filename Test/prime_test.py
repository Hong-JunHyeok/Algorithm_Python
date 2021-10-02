def print_prime():
    counter = 0
    ptr = 0
    prime = [None] * 1000

    prime[ptr] = 2
    ptr += 1

    for i in range(3, 1001, 2):
        for n in range(1, ptr):
            if i % prime[n] == 0:
                # 소수가 아닌 경우
                break
        else:
            prime[ptr] = i
            ptr += 1

    for i in range(ptr):
        print(prime[i])


if __name__ == "__main__":
    print_prime()
