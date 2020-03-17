def primes(n):
    """given a number, n, returns all prime numbers less than n"""
    import gmpy2
    n = 2
    while True:
        yield n
        n = gmpy2.next_prime(n)


def is_prime(n):
    """given a number, n, returns true if the number is prime and false"""
    primes_list = primes(n+1)
    print(primes_list)
    return n in primes_list
