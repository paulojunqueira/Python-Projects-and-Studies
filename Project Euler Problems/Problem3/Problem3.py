# Problem 3 https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

#Generatea list of all prime factors in a range of 2 to size
def genPrimes(size):
    primes = [i for i in range(2,size)]

    for i in range(len(primes)):
        for j in range(i+1,len(primes)):

            if primes[i] !=0 and primes[j] != 0:

                if (primes[j]%primes[i]) == 0:
                    primes[j] = 0

    for i in range(primes.count(0)):
        primes.remove(0)
    
    return primes

# Check prime factors of a number from a prvious list of Prime factors
def factors(num):
    primes = genPrimes(10000)
    factors = []
    for n in primes:

        if num%n == 0:
            num = num/n
            factors.append(n)
    return factors 

#Solution 
num = 600851475143
factors = factors(num)
print(f"Prime factors of {num} are: \n {factors}")