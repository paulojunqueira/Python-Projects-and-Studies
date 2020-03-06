#Problem  9 https://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def getPyth(sumation):
    for a  in range(1,sumation):
        num = a+1
        for b in range(num,sumation):
            p = a**2 + b**2
            s = (sumation - a - b)**2 
            if p - s == 0:
                c=sumation-a-b
                return [a,b,c]
           

             

a,b,c = (getPyth())
prod = a*b*c

getPyth(10000)