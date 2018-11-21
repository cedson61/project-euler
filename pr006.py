import time
 
def ss1(n):
    sum = ((n+1)*n)/2
    squared = sum**2
    return squared
 
def ss2 (n):
    sum = 0
    for i in range(n + 1):
        sum += i**2
    return sum
 
def difference(n):
    return ss1(n) - ss2(n)
 
start = time.time()

butthole = difference(100)

elapsed = time.time() - start

print ("%s found in %s seconds.") % (butthole,elapsed)

