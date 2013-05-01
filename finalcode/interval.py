import math
import numpy as np
from scipy.stats import norm
from scipy import special

#ratings are from 1 to 100
raterange = 100

def reject_outliers(data, m=2):
    if (len(set(data)) < 2):
        return data
    newdata = []
    for d in data:
        if (abs(d - np.mean(data)) < m * np.std(data)):
            newdata.append(d)
    return newdata

def conf(ratings):
    ratings =  reject_outliers(ratings)
    if (ratings == []):
        return 0.0
    if (np.std(ratings) == 0):
        if (len(ratings))>9:
            return 1.0
        else:
            return math.log(len(ratings))/2.1      
    intwid = 0.01
    perc = 1.0
    upper = 1.0
    lower = 0.0
    n = len(ratings)
    mean = sum(ratings)/n
    stdev = np.std(ratings)
    while (perc>intwid):
        z = norm.ppf(1-(intwid/2))
        lower = mean-(z*stdev/(math.sqrt(n)))
        upper = mean+(z*stdev/(math.sqrt(n)))
        perc = 0.0
        for v in ratings:
            perc += (special.ndtr((upper - v)/n)-special.ndtr((lower - v)/n))
        if (intwid == 1.0):
            return 0.0
        intwid += 0.01
        
    return 1-intwid

#a few examples
ratings = [1.0, 98.0, 45.0, 39.0, 12.0, 1.0, 98.0, 45.0, 39.0, 12.0, 1.0, 98.0, 45.0, 39.0, 12.0, 1.0, 98.0, 45.0, 39.0, 12.0, 1.0, 98.0, 45.0, 39.0, 12.0]
assert (int (100*conf(ratings)) == 18)

ratings = [29.0, 29.0, 29.0, 30.0, 31.0, 40.0, 45.0, 50.0, 51.0, 76.0, 90.0]
assert (int (100*conf(ratings)) == 25)

ratings = [1.0, 2.0, 50.0, 50.0, 90.0]
assert (int (100*conf(ratings)) == 41)

ratings = [45, 50, 50, 50, 50, 51, 52, 53]
assert (int (100*conf(ratings)) == 65)

ratings = [50, 50, 50, 50]
assert (int (100*conf(ratings)) == 66)

ratings = []
assert (int (100*conf(ratings)) == 0)

ratings = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
assert (int (100*conf(ratings)) == 100) 
