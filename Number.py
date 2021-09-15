import math

import random
from re import A

from tensorflow.python.keras.backend import maximum
maxite = 0
maxnum = 0
for a in range(1000000):
    iterations = 0
    

    num = a 
    
    while num > 1:
        iterations = iterations +1
        if (num % 2) == 0:
            num = num/2
        else:  
            num = num*3+1
    if iterations > maxite:
        maxite = iterations
        maxnum = a
print(maxite)
print(maxnum) #amongus
