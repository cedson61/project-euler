#dear god this is going to take forever


def isPrime(n):
	p = True
	z = n**0.5+1
	for x in primes:
		if (x >z):
			break
		if (n % x == 0):
			p = False
			return p
	return p

primes = [2]

for x in xrange(3, 200283825047, 2):
	if isPrime(x):
		print x
		primes.append(x)
print primes
