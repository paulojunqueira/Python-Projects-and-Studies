# # Problem 5  https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


upper = 20
re = [1]
num= upper

while sum(re) != 0 :
    start = 0
    num+=2
    re.clear()
    for n in range(1,upper+1):
        re.append(num%n)

    # print(f"Number tested:{num}, re: {sum(re)}")
print(num)
