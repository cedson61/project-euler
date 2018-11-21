import time


def solve():
    g = 380
    while True:
        b = True
        for x in range(11,20):
            if (g%x!=0):
                b = False
                break

        if (b):
            return g
            break
        g += 380
        print g




start = time.time()

butthole = solve()

elapsed = time.time() - start

print ("%s found in %s seconds.") % (butthole,elapsed)

