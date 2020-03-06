# Problem 10 https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

#From Previous Problem
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
below = 2000000
primes = []
while num < below:
    if isPrime(num):
        i +=1
        primes.append(num)
    num+=1


print(f'Sum of primes below {below} is {sum(primes)}')
