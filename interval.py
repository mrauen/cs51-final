#ratings are from 1 to 100
raterange = 99

def conf(ratings):
    interval = (ratings[-1]-ratings[0])/raterange
    c = float (len(ratings))
    perc = 1.0
    mean = float (raterange/2)
    inside = ratings
    while (perc>interval):
        if ((mean-inside[0])>(inside[-1]-mean)):
            interval = float (2.0*(mean-inside[0])/raterange)
            inside = inside[1:]
        else:
            interval = float (2.0*(inside[-1]-mean)/raterange)
            inside = inside[:-1]
        perc = float (len(inside)/c)
        if (interval == 0.0):
            return 1.0
    return 1-interval
