# Peak finding Algorithm 

import numpy as np 
import matplotlib.pyplot as plt
from time import perf_counter, clock , process_time

def peak_(array):
    ok = True
    peak = 0
    # start = np.random.randint(0, len(array))
    i = 0
    while ok:

        p = array[i]

        if (i == 0):
            if p >= array[i+1]:
                peak = p
                ok = False
        elif i == (len(array)-1):
            peak = p
            ok = False
        else:
            if p>= array[i-1] and p>= array[i+1]:
                peak = p
                ok = False
        
        i+=1

    return peak



def peak_2(array):

    ok = True
    peak = 0
    i = round(len(array)/2)

    while ok :
        p = array[i]
        if i == 0 or (i == (len(array)-1)):
            peak = p
            ok = False
        elif p < array[i-1]:
            i-=1
        elif p < array[i+1]:
            i+=1
        else: 
            peak = p
            ok = False
    return peak


array = [9,3,2,1,0,5,2]
array = np.random.randint(0,100,100)
array = np.arange(1, 10)
peak_2(array)
peak_(array)



plt.figure(figsize = (12,8))
plt.plot(array)



k = np.arange(100, 1000)
mean1 = []
mean2 = []
for ki in k:
    num1 = []
    num2 = []
    array = np.arange(0,ki)
    for t in range(100):
        start = perf_counter()
        re1 = peak_(array)
        end = perf_counter()
        num1.append(round((end-start),4))

        start = perf_counter()
        re2 = peak_2(array)
        end = perf_counter()
        num2.append(round((end-start),4))



    mean1.append(np.mean(num1))
    mean2.append(np.mean(num2))

plt.figure(figsize = (12,6))
plt.plot(mean1, label = '1')
plt.plot(mean2, label = '2')
plt.ylabel('t')
plt.xlabel('Size')
plt.legend()

import math
x = np.arange(1,10)
y = list(map(math.log10, x))
plt.plot(x,y)
plt.plot(x,x)