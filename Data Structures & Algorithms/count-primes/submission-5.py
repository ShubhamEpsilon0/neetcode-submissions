import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        primes = [1] * (n)

        # 0 and 1 are not prime numbers
        primes[0] = primes[1] = 0

        for i in range(2, int(math.sqrt(n)) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = 0
        return sum(primes)
        # count = 0
        # if n <= 2:
        #     return 0
        # if n == 3:
        #     return 1
        # primes = [2, 3]
        # for i in range(4, n):
        #     is_prime = True
        #     for prime in primes:
        #         if i % prime == 0:
        #             is_prime = False
        #             break
        #     if is_prime:
        #         primes.append(i)
        # return len(primes)
        