def max_of(n):
    maximum = n[0]
    for i in range(1, len(n)):
        if n[i] > maximum:
            maximum = n[i]
    return maximum


print(max_of([1, 2, 3, 2, 42, 5, 1, 2, 3, 10]))
