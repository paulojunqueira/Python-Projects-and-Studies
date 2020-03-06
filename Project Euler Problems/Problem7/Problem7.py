# # Problem 7 https://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# From previous Problem 3
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

# Main
primes= genPrimes(125000)
len(primes)
primes[10000]

####### 2) Faster Prime Checker ######

#Faster Prime Checker
def isPrime(num):
    if num <= 1:
        return False
        
    elif num <= 3:
        return True
    elif num%2 == 0 or num%3 == 0:
        return False 

    i = 5
    while (i*i) <= num :
        if (num%i == 0) or (num%(i+2) == 0):
            return False
        i = i + 6

    return True

# Main
num = 1 
i = 0
primes = []
while i <= 10000:

    if isPrime(num):
        i +=1
        primes.append(num)
    num+=1

primes[-1]