# # Problem 4 https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def findPalindromes(d):
    a = 10**(d-1)
    b = 10**(d)-1
    numbers = [str(i*j) for i in range(a,b) for j in range(a,b)]

    palindromes = []
    for s in numbers:
        if s == s[::-1]:
            palindromes.append(int(s))

    return palindromes



d = 5 # d-digits of two numbers
palindromes = findPalindromes(d)

print(f"The largest palindrome of {d} digits is:{max(palindromes)}")