import time
 

def nth_prime(n):
	prime = 2
	by = 1
	iter = 3
	while by < n:
		if isprime(iter):
			prime = iter
			by += 1
		iter += 2
	return prime

def isprime(n):
	while True:
		b = True
		if n % 2 == 0:
		 b = False
		if n % 5 == 0:
		 b = False
		d = 3
		while d < (n**0.5)+1:
			if n % d == 0: b = False
			d += 2
		print d
		return b
 
start = time.time()
butthole = nth_prime(10001)
elapsed = time.time() - start

print ("%s found in %s seconds. eat pant euler.") % (butthole,elapsed)
