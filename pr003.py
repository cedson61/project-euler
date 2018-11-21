import time

def solve():
    n = 600851475143
    while True:
        p = lpf(n)
        if p < n:
            n //= p
        else:
            return str(n)

def lpf(n):
    assert n >= 2
    for i in range(2, sqrt(n) + 1):
        if n % i == 0:
            return i
    return n  
def sqrt(x):
    assert x >= 0
    i = 1
    while i * i <= x:
        i *= 2
    y = 0
    while i > 0:
        if (y + i)**2 <= x:
            y += i
        i //= 2
    return y

start = time.time()

butthole = solve()

elapsed = time.time() - start

print ("%s found in %s seconds.") % (butthole,elapsed)

