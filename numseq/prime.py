def primes(n):
    """given a number, n, returns all prime numbers less than n"""
    import math
    if n < 2:
        return []
    else:
        primes = [2]
        if n <= primes[-1]:
            return primes
        else:
            for index in range(3, n, 2):
                isPrime = True
                for primenumber in primes:
                    if not index % primenumber:
                        isPrime = False
                if isPrime:
                    primes.append(index)


def is_prime(n):
    """given a number, n, returns true if the number is prime and\
false if it's not"""
    primes_list = primes(n+1)
    print(primes_list)
    return n in primes_list

print(is_prime(3))