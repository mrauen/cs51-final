#ratings are from 1 to 10
raterange = 9

def conf(ratings):
    interval = (ratings[-1]-ratings[0])/raterange
    c = len(ratings)
    perc = 1.0
    mean = sum(ratings)/c
    inside = ratings
    while (perc>interval):
        if ((mean-inside[0])>(inside[-1]-mean)):
            inside = inside[1:]
        else:
            inside = inside[:-1]
        interval = (inside[-1]-inside[0])
        perc = len(inside)/c
    return 1-perc
