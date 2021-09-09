# largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# python problem-3.py

import sympy as sp

N = 30
# P = int(N/(10^(len(str(abs(N))))-1))
# print(P)
M = N
prime_no = list(sp.primerange(0, N))

print('finding largest prime factor of ', N)
prime_factors = []

print(prime_no)

for i in prime_no:
    if N % i == 0:
        N = N/i
        print('current largest prime: ', i)
        prime_factors.append(i)
        n = prime_no.index(i)
        del prime_no[0:n]
        print(prime_no)
        print('remaining: ', N)
        continue
    elif N/i == 1:
        prime_factors.append(i)
        break
    else:
        pass       

print('prime factors of ', M, ': ', prime_factors)
print('largest prime factor: ', max(prime_factors))