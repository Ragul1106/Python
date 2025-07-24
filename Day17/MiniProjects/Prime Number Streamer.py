def prime_generator(limit):
    yield 2
    primes = [2]
    candidate = 3
    while candidate <= limit:
        is_prime = True
        for prime in primes:
            if prime * prime > candidate:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
            yield candidate
        candidate += 2  

for prime in prime_generator(100):
    print(prime, end=' ')