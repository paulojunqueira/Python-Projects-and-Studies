# Peak finding Algorithm 

import numpy as np 
import matplotlib.pyplot as plt


def peak_1(array):
    """ Function that finds a peak 
        
        Input:
            -array: a list containing data
        Return:
            -Returns a peak
    """

    ok = True
    peak = 0
    
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
    """ Function that finds a peak 
        Suposed to be faster than peak_1()

        Input:
            -array: a list containing data
        Return:
            -Returns a peak
    """

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

def peaksFinder(array):
    """ Function that finds all peaks
        
        Input:
            -array: a list containing data
        Return:
            -Returns a tuple containing the position and the value of 
             the peak.
    """

    peaks = []    
    for i, p in enumerate(array):
        
        if (i == 0):
            if p >= array[i+1]:
                peaks.append((i,p))
                
        elif i == (len(array)-1) and p > array[i-1]:
            peaks.append((i,p))
        else:
            if p>= array[i-1] and p>= array[i+1]:
                peaks.append((i,p))
            

    return peaks

def peaksThreshold(array, threshold):
    """ Function that finds peaks above a threshold
        
        Input:
            -array: a list containing data
            -threshold: define the value of threshold
        Return:
            -Returns a tuple containing the position and the value of 
             the peak above threshold. 
    """

    peaks = []
       
    for i, p in enumerate(array):
        
        if (p > threshold):
            if (i == 0):
                if (p >= array[i+1]) :
                    peaks.append((i,p))
                    
            elif (i == (len(array)-1)) and (p > array[i-1]):
                peaks.append((i,p))
            else:
                if p>= array[i-1] and p>= array[i+1]:
                    peaks.append((i,p))
            

    return peaks




array_1 = np.arange(1,100)
array_2 = np.random.choice(100, 100, replace = False)
#Find a Peak
peak_11 = peak_1(array_1)
peak_21 = peak_1(array_2)
#Find a Peak Faster
peak_12 = peak_2(array_1)
peak_22 = peak_2(array_2)


nPoints = 200
varMin = 0
varMax = 100
threshold = 80
array = np.random.randint(varMin,varMax,nPoints)


# Find all Peaks
peaks = peaksFinder(array)
x, y = zip(*peaks)
plt.figure(figsize = (12,6))
plt.plot(array)
plt.scatter(x, y,  marker = 'x', c = 'red', linewidths=20)
plt.title('Find Peaks')
plt.show()


# Find Peak above a threshold
peaks = peaksThreshold(array, threshold)
plt.figure(figsize = (12,6))
plt.plot(array)
plt.axhline(y=threshold, color='r', linestyle='--')
x, y = zip(*peaks)
plt.scatter(x, y,  marker = 'x', c = 'red', linewidths=20)
plt.title('Find Peaks above Threshold')
plt.show()





