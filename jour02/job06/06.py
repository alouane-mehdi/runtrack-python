for n in range(1, 1001):
    i = 2
    while i*i <= n and n % i != 0:
        i = i + 1
    if i*i > n and n > 1:
        print(n)
